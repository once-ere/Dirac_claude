//! Natural cubic spline on a uniform grid (the potentials M_eff(y) and
//! v_x(y) of the Kohn-Sham equation are tabulated on the y grid and the
//! CVODE right-hand side evaluates them between the nodes).
//!
//! Second derivatives from the tridiagonal system with natural end
//! conditions (Thomas algorithm, deterministic); evaluation is clamped to the
//! grid.

#[derive(Clone, Debug, PartialEq)]
pub struct Spline {
    pub y0: f64,
    pub dy: f64,
    pub values: Vec<f64>,
    second: Vec<f64>,
}

impl Spline {
    /// Build from values at y0 + i dy, i = 0..n-1 (n >= 2).
    pub fn new(y0: f64, dy: f64, values: Vec<f64>) -> Self {
        let n = values.len();
        let mut second = vec![0.0; n];
        if n >= 3 {
            let m = n - 2;
            let mut diag = vec![4.0; m];
            let mut rhs = vec![0.0; m];
            for i in 0..m {
                rhs[i] = 6.0 * (values[i + 2] - 2.0 * values[i + 1] + values[i]) / (dy * dy);
            }
            // Thomas algorithm, sub/super diagonals = 1
            for i in 1..m {
                let factor = 1.0 / diag[i - 1];
                diag[i] -= factor;
                rhs[i] -= factor * rhs[i - 1];
            }
            let mut x = vec![0.0; m];
            x[m - 1] = rhs[m - 1] / diag[m - 1];
            for i in (0..m - 1).rev() {
                x[i] = (rhs[i] - x[i + 1]) / diag[i];
            }
            second[1..(m + 1)].copy_from_slice(&x[..m]);
        }
        Self {
            y0,
            dy,
            values,
            second,
        }
    }

    pub fn constant(y0: f64, dy: f64, n: usize, value: f64) -> Self {
        Self::new(y0, dy, vec![value; n])
    }

    pub fn len(&self) -> usize {
        self.values.len()
    }

    pub fn is_empty(&self) -> bool {
        self.values.is_empty()
    }

    pub fn eval(&self, y: f64) -> f64 {
        let n = self.values.len();
        if n == 1 {
            return self.values[0];
        }
        let position = (y - self.y0) / self.dy;
        let mut i = position.floor() as i64;
        if i < 0 {
            i = 0;
        }
        if i > (n as i64) - 2 {
            i = (n as i64) - 2;
        }
        let i = i as usize;
        let a = (self.y0 + (i as f64 + 1.0) * self.dy - y) / self.dy;
        let b = 1.0 - a;
        a * self.values[i]
            + b * self.values[i + 1]
            + ((a * a * a - a) * self.second[i] + (b * b * b - b) * self.second[i + 1])
                * self.dy
                * self.dy
                / 6.0
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::math::sin;

    #[test]
    fn reproduces_nodes_and_interpolates_smoothly() {
        let n = 101;
        let dy = 0.03;
        let values: Vec<f64> = (0..n).map(|i| sin(-3.0 + i as f64 * dy)).collect();
        let s = Spline::new(-3.0, dy, values.clone());
        for (i, v) in values.iter().enumerate() {
            assert!((s.eval(-3.0 + i as f64 * dy) - v).abs() < 1e-14);
        }
        let mut worst: f64 = 0.0;
        for j in 0..1000 {
            let y = -2.9 + j as f64 * 0.0028;
            worst = worst.max((s.eval(y) - sin(y)).abs());
        }
        assert!(worst < 2e-7, "{worst}");
        let c = Spline::constant(0.0, 0.1, 5, 2.5);
        assert_eq!(c.eval(0.23), 2.5);
    }
}
