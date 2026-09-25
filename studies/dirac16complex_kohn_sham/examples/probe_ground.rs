use dirac16complex_kohn_sham::scf::{solve_ground, standard_params};
fn main() {
    for (name, m, lh, t, n) in [("N1016 lamm2 (crossing)", 1.0, -1.5769e-3, 0.0, 1016.0), ("N1016 lamp2 (exact)", 1.0, 1.5769e-3, 0.0, 1016.0), ("N112 lam0 T0.1", 1.0, 0.0, 0.1, 112.0), ("N112 lam0 T1.0", 1.0, 0.0, 1.0, 112.0)] {
        let start = std::time::Instant::now();
        let p = standard_params(m, 3.0, lh, t, n);
        match solve_ground(&p, None, 0.0) {
            Ok(s) => {
                let frac = s.spectrum.states.iter().filter(|st| st.branch > 0 && st.f > 1e-6 && st.f < 1.0 - 1e-6).count();
                println!("{name}: converged {} smearing {} it {} E {:.10} F {:.10} S_ent {:.4e} mu {:.8} gap {:?} N {} states {} window [{:.3},{:.3}] fractional {} |lamS|/m {:.4} |vx|/m {:.4} ({:?})", s.converged, s.params.smearing, s.iterations, s.energies.total, s.energies.free, s.energies.entropy, s.filling.mu, s.gap(), s.energies.n_total, s.spectrum.states.len(), s.window.eps_lo, s.window.eps_hi, frac, s.energies.max_lambda_s_over_m, s.energies.max_v_x_over_m, start.elapsed());
            }
            Err(e) => println!("{name}: ERROR {e}"),
        }
    }
}
