//! Reusable CVODE driver (pure-Rust SUNDIALS 7.8.0).
//!
//! `integrate(y0, t0, targets, rhs, cfg)` integrates `y' = f(t, y)` from `t0`
//! through the output times `targets` (strictly monotone, all on the same side
//! of `t0`; decreasing targets integrate backward) and returns the state at
//! `t0` followed by the state at every target.
//!
//! * The right-hand side is an ordinary Rust closure.  CVODE callbacks are
//!   plain `fn` pointers, so the closure travels through CVODE's `user_data`
//!   (`Box<dyn Any>`) and a trampoline `fn` downcasts it and calls it
//!   (the verified closure-trampoline pattern of the solver survey).
//! * The state/derivative guards returned by `N_VGetArrayPointer` are
//!   `RefMut`s; they only live inside the trampoline and inside short blocks
//!   here, never across a solver call.
//! * Method choice (documented in every summary.json via `describe()`):
//!   - `Method::Bdf`: CVODE BDF with the default Newton nonlinear solver and
//!     the dense direct linear solver (`SUNDenseMatrix` + `SUNLinSol_Dense`)
//!     with CVODE's internal difference-quotient Jacobian.  House style of
//!     dirac-main and planet_Mercury.
//!   - `Method::Adams`: CVODE Adams-Moulton with the fixed-point (functional)
//!     nonlinear solver `SUNNonlinSol_FixedPoint(y, 0)` (no Anderson
//!     acceleration, no linear solver).  This is the classical choice for
//!     non-stiff, oscillatory problems such as the spinor mode equations,
//!     whose Jacobian `-i h` has purely imaginary (or, in EXP-5, real and
//!     moderate) eigenvalues.
//! * Every SUNDIALS return flag is checked and turned into a named error.
//!   Teardown is in the C order (CVodeFree, SUNNonlinSolFree,
//!   SUNLinSolFree, SUNMatDestroy, N_VDestroy(abstol), N_VDestroy(y),
//!   SUNContext_Free) on the success path and on every error path after the
//!   objects exist.
//! * Closure errors: `Err(message)` from the closure aborts the integration
//!   (the trampoline returns -1, unrecoverable) and the message is reported;
//!   a non-finite derivative returns 1 (recoverable: CVODE retries with a
//!   smaller step).

use std::any::Any;

use cvode_rs::prelude::*;

/// Linear multistep family.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum Method {
    /// BDF + Newton + dense direct linear solver (DQ Jacobian).
    Bdf,
    /// Adams-Moulton + fixed-point (functional) iteration.
    Adams,
}

/// Absolute tolerance: one scalar or one value per state component.
#[derive(Clone, Debug, PartialEq)]
pub enum AbsTol {
    Scalar(f64),
    Vector(Vec<f64>),
}

/// Solver configuration of one integration.
#[derive(Clone, Debug, PartialEq)]
pub struct SolverConfig {
    pub method: Method,
    pub rtol: f64,
    pub atol: AbsTol,
    /// Maximum step size; 0.0 means "no limit" (CVODE default).
    pub max_step: f64,
    /// CVodeSetMaxNumSteps (maximum internal steps per output call).
    pub max_num_steps: i64,
    /// CVodeSetStopTime; `None` lets CVODE integrate past the last target
    /// internally and interpolate back.
    pub stop_time: Option<f64>,
}

impl SolverConfig {
    pub fn bdf(rtol: f64, atol: f64, max_step: f64) -> Self {
        Self {
            method: Method::Bdf,
            rtol,
            atol: AbsTol::Scalar(atol),
            max_step,
            max_num_steps: 1_000_000,
            stop_time: None,
        }
    }

    pub fn adams(rtol: f64, atol: f64, max_step: f64) -> Self {
        Self {
            method: Method::Adams,
            ..Self::bdf(rtol, atol, max_step)
        }
    }

    pub fn with_stop_time(mut self, stop_time: f64) -> Self {
        self.stop_time = Some(stop_time);
        self
    }

    /// Human/JSON-readable description of the method and nonlinear solver.
    pub fn describe(&self) -> &'static str {
        match self.method {
            Method::Bdf => "CVODE BDF + Newton + dense direct linear solver (DQ Jacobian)",
            Method::Adams => "CVODE Adams-Moulton + fixed-point (functional) iteration",
        }
    }
}

/// Boxed right-hand side `rhs(t, y, ydot)`.
pub type RhsFn = Box<dyn FnMut(f64, &[f64], &mut [f64]) -> Result<(), String>>;

/// Result of one integration.
#[derive(Clone, Debug, Default)]
pub struct Integration {
    /// `times[0] = t0`, then the time returned by CVode for every target.
    pub times: Vec<f64>,
    /// `states[i]` is the state at `times[i]`.
    pub states: Vec<Vec<f64>>,
    pub steps: i64,
    pub rhs_evals: i64,
    /// RHS evaluations spent on the difference-quotient Jacobian (BDF only).
    pub lin_rhs_evals: i64,
    pub jac_evals: i64,
    pub lin_setups: i64,
    pub err_test_fails: i64,
    pub nonlin_iters: i64,
    pub nonlin_conv_fails: i64,
    pub last_order: i32,
    pub last_step: f64,
}

/// What travels through CVODE's user_data.
struct ClosureData {
    rhs: RhsFn,
    error: Option<String>,
}

/// The CVRhsFn trampoline: downcast user_data and call the closure.
fn trampoline(t: f64, y: &N_Vector, ydot: &N_Vector, user_data: &mut Option<Box<dyn Any>>) -> i32 {
    let data = match user_data
        .as_mut()
        .and_then(|boxed| boxed.downcast_mut::<ClosureData>())
    {
        Some(data) => data,
        None => return -1,
    };
    let state = match N_VGetArrayPointer(y) {
        Some(state) => state,
        None => {
            data.error = Some("N_VGetArrayPointer returned None for y".to_string());
            return -1;
        }
    };
    let mut derivative = match N_VGetArrayPointer(ydot) {
        Some(derivative) => derivative,
        None => {
            data.error = Some("N_VGetArrayPointer returned None for ydot".to_string());
            return -1;
        }
    };
    match (data.rhs)(t, &state[..], &mut derivative[..]) {
        Ok(()) => {
            if derivative.iter().all(|value| value.is_finite()) {
                0
            } else {
                1
            }
        }
        Err(message) => {
            data.error = Some(message);
            -1
        }
    }
}

/// All solver objects, torn down in the C order.
struct Resources {
    context: Option<SUNContext>,
    y: Option<N_Vector>,
    abstol: Option<N_Vector>,
    cvode: Option<CVodeMem>,
    matrix: Option<SUNMatrix>,
    linear_solver: Option<SUNLinearSolver>,
    nonlinear_solver: Option<SUNNonlinearSolver>,
}

impl Resources {
    fn teardown(mut self) {
        if self.cvode.is_some() {
            CVodeFree(&mut self.cvode);
        }
        if let Some(nls) = self.nonlinear_solver.take() {
            let _ = SUNNonlinSolFree(Some(nls));
        }
        if let Some(ls) = self.linear_solver.take() {
            let _ = SUNLinSolFree(Some(ls));
        }
        if let Some(matrix) = self.matrix.take() {
            SUNMatDestroy(matrix);
        }
        if let Some(abstol) = self.abstol.take() {
            N_VDestroy(abstol);
        }
        if let Some(y) = self.y.take() {
            N_VDestroy(y);
        }
        if self.context.is_some() {
            let _ = SUNContext_Free(&mut self.context);
        }
    }
}

fn flag_check(flag: i32, name: &str) -> Result<(), String> {
    if flag == CV_SUCCESS {
        Ok(())
    } else {
        Err(format!("{name} failed with flag {flag}"))
    }
}

fn validate(y0: &[f64], t0: f64, targets: &[f64], cfg: &SolverConfig) -> Result<f64, String> {
    if y0.is_empty() {
        return Err("integrate: empty initial state".to_string());
    }
    if y0.iter().any(|value| !value.is_finite()) || !t0.is_finite() {
        return Err("integrate: non-finite initial data".to_string());
    }
    if targets.is_empty() {
        return Err("integrate: no output targets".to_string());
    }
    let direction = if targets[0] > t0 {
        1.0
    } else if targets[0] < t0 {
        -1.0
    } else {
        return Err("integrate: first target equals t0".to_string());
    };
    let mut previous = t0;
    for &target in targets {
        if !target.is_finite() || (target - previous) * direction <= 0.0 {
            return Err(format!(
                "integrate: targets must be finite and strictly monotone away from t0 \
                 (offending target {target})"
            ));
        }
        previous = target;
    }
    if !(cfg.rtol > 0.0 && cfg.rtol.is_finite()) {
        return Err("integrate: rtol must be finite and positive".to_string());
    }
    match &cfg.atol {
        AbsTol::Scalar(atol) => {
            if !(*atol > 0.0 && atol.is_finite()) {
                return Err("integrate: atol must be finite and positive".to_string());
            }
        }
        AbsTol::Vector(atol) => {
            if atol.len() != y0.len() || atol.iter().any(|a| !(*a > 0.0 && a.is_finite())) {
                return Err("integrate: vector atol must match the state and be positive".into());
            }
        }
    }
    if !(cfg.max_step >= 0.0 && cfg.max_step.is_finite()) {
        return Err("integrate: max_step must be finite and >= 0".to_string());
    }
    if cfg.max_num_steps <= 0 {
        return Err("integrate: max_num_steps must be positive".to_string());
    }
    if let Some(stop) = cfg.stop_time {
        let last = targets[targets.len() - 1];
        if !stop.is_finite() || (stop - last) * direction < 0.0 {
            return Err("integrate: stop_time must not precede the last target".to_string());
        }
    }
    Ok(direction)
}

fn read_vector(vector: &N_Vector, n: usize) -> Result<Vec<f64>, String> {
    let data = N_VGetArrayPointer(vector)
        .ok_or_else(|| "N_VGetArrayPointer returned None for y".to_string())?;
    Ok(data[..n].to_vec())
}

fn build(
    resources: &mut Resources,
    y0: &[f64],
    t0: f64,
    rhs: RhsFn,
    cfg: &SolverConfig,
) -> Result<(), String> {
    let n = y0.len();
    let mut context_output: Option<SUNContext> = None;
    let flag = SUNContext_Create(SUN_COMM_NULL, &mut context_output);
    if flag != 0 {
        return Err(format!("SUNContext_Create failed with flag {flag}"));
    }
    let context =
        context_output.ok_or_else(|| "SUNContext_Create returned no context".to_string())?;
    resources.context = Some(context.clone());

    let y = N_VNew_Serial(n as i64, &context)
        .ok_or_else(|| "N_VNew_Serial(y) returned None".to_string())?;
    {
        let mut data = N_VGetArrayPointer(&y)
            .ok_or_else(|| "N_VGetArrayPointer returned None for y".to_string())?;
        data[..n].copy_from_slice(y0);
    }
    resources.y = Some(y.clone());

    let lmm = match cfg.method {
        Method::Bdf => CV_BDF,
        Method::Adams => CV_ADAMS,
    };
    let cvode =
        CVodeCreate(lmm, &context).ok_or_else(|| "CVodeCreate returned None".to_string())?;
    resources.cvode = Some(cvode.clone());
    flag_check(CVodeInit(&cvode, trampoline, t0, &y), "CVodeInit")?;

    match &cfg.atol {
        AbsTol::Scalar(atol) => {
            flag_check(
                CVodeSStolerances(&cvode, cfg.rtol, *atol),
                "CVodeSStolerances",
            )?;
        }
        AbsTol::Vector(atol) => {
            let abstol = N_VNew_Serial(n as i64, &context)
                .ok_or_else(|| "N_VNew_Serial(abstol) returned None".to_string())?;
            {
                let mut data = N_VGetArrayPointer(&abstol)
                    .ok_or_else(|| "N_VGetArrayPointer returned None for abstol".to_string())?;
                data[..n].copy_from_slice(atol);
            }
            resources.abstol = Some(abstol.clone());
            flag_check(
                CVodeSVtolerances(&cvode, cfg.rtol, &abstol),
                "CVodeSVtolerances",
            )?;
        }
    }

    match cfg.method {
        Method::Bdf => {
            let matrix = SUNDenseMatrix(n as i64, n as i64, &context)
                .ok_or_else(|| "SUNDenseMatrix returned None".to_string())?;
            resources.matrix = Some(matrix.clone());
            let linear_solver = SUNLinSol_Dense(&y, &matrix, &context)
                .ok_or_else(|| "SUNLinSol_Dense returned None".to_string())?;
            resources.linear_solver = Some(linear_solver.clone());
            flag_check(
                CVodeSetLinearSolver(&cvode, &linear_solver, Some(&matrix)),
                "CVodeSetLinearSolver",
            )?;
        }
        Method::Adams => {
            let nonlinear_solver = SUNNonlinSol_FixedPoint(&y, 0, &context)
                .ok_or_else(|| "SUNNonlinSol_FixedPoint returned None".to_string())?;
            resources.nonlinear_solver = Some(nonlinear_solver.clone());
            flag_check(
                CVodeSetNonlinearSolver(&cvode, &nonlinear_solver),
                "CVodeSetNonlinearSolver",
            )?;
        }
    }

    let user: Box<dyn Any> = Box::new(ClosureData { rhs, error: None });
    flag_check(CVodeSetUserData(&cvode, Some(user)), "CVodeSetUserData")?;
    flag_check(
        CVodeSetMaxNumSteps(&cvode, cfg.max_num_steps),
        "CVodeSetMaxNumSteps",
    )?;
    if cfg.max_step > 0.0 {
        flag_check(CVodeSetMaxStep(&cvode, cfg.max_step), "CVodeSetMaxStep")?;
    }
    if let Some(stop) = cfg.stop_time {
        flag_check(CVodeSetStopTime(&cvode, stop), "CVodeSetStopTime")?;
    }
    Ok(())
}

/// The closure's error message, if it reported one (swaps user_data out and
/// back in, as CVodeGetUserData requires).
fn closure_error(cvode: &CVodeMem) -> Option<String> {
    let mut user: Option<Box<dyn Any>> = None;
    if CVodeGetUserData(cvode, &mut user) != CV_SUCCESS {
        return None;
    }
    let message = user
        .as_mut()
        .and_then(|boxed| boxed.downcast_mut::<ClosureData>())
        .and_then(|data| data.error.take());
    let _ = CVodeSetUserData(cvode, user);
    message
}

fn march(
    resources: &Resources,
    n: usize,
    t0: f64,
    targets: &[f64],
    y0: &[f64],
) -> Result<Integration, String> {
    let cvode = resources
        .cvode
        .as_ref()
        .ok_or_else(|| "internal: CVODE memory missing".to_string())?;
    let y = resources
        .y
        .as_ref()
        .ok_or_else(|| "internal: state vector missing".to_string())?;
    let mut result = Integration {
        times: vec![t0],
        states: vec![y0.to_vec()],
        ..Integration::default()
    };
    let mut t = t0;
    for &target in targets {
        let flag = CVode(cvode, target, y, &mut t, CV_NORMAL);
        if flag < 0 {
            let reason = closure_error(cvode)
                .map(|message| format!(" (rhs: {message})"))
                .unwrap_or_default();
            return Err(format!(
                "CVode failed with flag {flag} at t = {t} heading for {target}{reason}"
            ));
        }
        result.times.push(t);
        result.states.push(read_vector(y, n)?);
    }
    flag_check(
        CVodeGetNumSteps(cvode, &mut result.steps),
        "CVodeGetNumSteps",
    )?;
    flag_check(
        CVodeGetNumRhsEvals(cvode, &mut result.rhs_evals),
        "CVodeGetNumRhsEvals",
    )?;
    flag_check(
        CVodeGetNumErrTestFails(cvode, &mut result.err_test_fails),
        "CVodeGetNumErrTestFails",
    )?;
    flag_check(
        CVodeGetNumNonlinSolvIters(cvode, &mut result.nonlin_iters),
        "CVodeGetNumNonlinSolvIters",
    )?;
    flag_check(
        CVodeGetNumNonlinSolvConvFails(cvode, &mut result.nonlin_conv_fails),
        "CVodeGetNumNonlinSolvConvFails",
    )?;
    flag_check(
        CVodeGetLastOrder(cvode, &mut result.last_order),
        "CVodeGetLastOrder",
    )?;
    flag_check(
        CVodeGetLastStep(cvode, &mut result.last_step),
        "CVodeGetLastStep",
    )?;
    if resources.linear_solver.is_some() {
        flag_check(
            CVodeGetNumJacEvals(cvode, &mut result.jac_evals),
            "CVodeGetNumJacEvals",
        )?;
        flag_check(
            CVodeGetNumLinRhsEvals(cvode, &mut result.lin_rhs_evals),
            "CVodeGetNumLinRhsEvals",
        )?;
        flag_check(
            CVodeGetNumLinSolvSetups(cvode, &mut result.lin_setups),
            "CVodeGetNumLinSolvSetups",
        )?;
    }
    Ok(result)
}

/// Integrate `y' = rhs(t, y)` from `(t0, y0)` through `targets`.
pub fn integrate(
    y0: Vec<f64>,
    t0: f64,
    targets: &[f64],
    rhs: RhsFn,
    cfg: &SolverConfig,
) -> Result<Integration, String> {
    validate(&y0, t0, targets, cfg)?;
    let mut resources = Resources {
        context: None,
        y: None,
        abstol: None,
        cvode: None,
        matrix: None,
        linear_solver: None,
        nonlinear_solver: None,
    };
    let outcome = build(&mut resources, &y0, t0, rhs, cfg)
        .and_then(|()| march(&resources, y0.len(), t0, targets, &y0));
    resources.teardown();
    outcome
}

/// Backward integration: `targets` must be strictly decreasing and below t0.
pub fn integrate_backward(
    y0: Vec<f64>,
    t0: f64,
    targets: &[f64],
    rhs: RhsFn,
    cfg: &SolverConfig,
) -> Result<Integration, String> {
    if targets.first().is_none_or(|&first| first >= t0) {
        return Err("integrate_backward: targets must lie below t0".to_string());
    }
    integrate(y0, t0, targets, rhs, cfg)
}

/// `count` equally spaced targets `t0 + (t1 - t0) i / count`, i = 1..=count
/// (exact end point, no accumulated rounding).
pub fn uniform_targets(t0: f64, t1: f64, count: usize) -> Vec<f64> {
    (1..=count)
        .map(|index| {
            if index == count {
                t1
            } else {
                t0 + (t1 - t0) * (index as f64) / (count as f64)
            }
        })
        .collect()
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::math::{cos, sin};

    fn oscillator() -> RhsFn {
        Box::new(|_t, y, ydot| {
            ydot[0] = y[1];
            ydot[1] = -y[0];
            Ok(())
        })
    }

    #[test]
    fn harmonic_oscillator_forward_both_methods() {
        let targets = uniform_targets(0.0, 10.0, 20);
        for cfg in [
            SolverConfig::bdf(1e-10, 1e-12, 0.05),
            SolverConfig::adams(1e-10, 1e-12, 0.05).with_stop_time(10.0),
        ] {
            let run = integrate(vec![1.0, 0.0], 0.0, &targets, oscillator(), &cfg).unwrap();
            assert_eq!(run.times.len(), 21);
            assert_eq!(run.times[20], 10.0);
            for (t, y) in run.times.iter().zip(&run.states) {
                assert!((y[0] - cos(*t)).abs() < 1e-7, "{:?} at {t}", cfg.method);
                assert!((y[1] + sin(*t)).abs() < 1e-7);
            }
            assert!(run.steps > 0 && run.rhs_evals > 0);
        }
    }

    #[test]
    fn harmonic_oscillator_backward_and_vector_atol() {
        let targets: Vec<f64> = (1..=10).map(|i| -0.5 * i as f64).collect();
        let mut cfg = SolverConfig::bdf(1e-10, 1e-12, 0.05);
        cfg.atol = AbsTol::Vector(vec![1e-12, 1e-12]);
        let run = integrate_backward(vec![1.0, 0.0], 0.0, &targets, oscillator(), &cfg).unwrap();
        for (t, y) in run.times.iter().zip(&run.states) {
            assert!((y[0] - cos(*t)).abs() < 1e-7);
            assert!((y[1] + sin(*t)).abs() < 1e-7);
        }
        assert!(integrate_backward(vec![1.0, 0.0], 0.0, &[1.0], oscillator(), &cfg).is_err());
    }

    #[test]
    fn closure_error_is_reported_and_targets_validated() {
        let rhs: RhsFn = Box::new(|t, _y, ydot| {
            if t > 0.5 {
                Err("deliberate failure".to_string())
            } else {
                ydot[0] = 1.0;
                Ok(())
            }
        });
        let cfg = SolverConfig::bdf(1e-8, 1e-10, 0.01);
        let error = integrate(vec![0.0], 0.0, &[1.0], rhs, &cfg).unwrap_err();
        assert!(error.contains("deliberate failure"), "{error}");
        let error = integrate(vec![0.0], 0.0, &[1.0, 0.5], oscillator(), &cfg).unwrap_err();
        assert!(error.contains("monotone"), "{error}");
    }
}
