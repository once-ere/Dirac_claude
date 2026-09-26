use dirac16complex_kohn_sham::scf::{solve_ground, standard_params};
fn main() {
    for (name, lh) in [("N8 lam0 T1.0", 0.0), ("N8 lamp1 T1.0", 9.7299e-3)] {
        let start = std::time::Instant::now();
        let p = standard_params(1.0, 3.0, lh, 1.0, 8.0);
        match solve_ground(&p, None, 0.0) {
            Ok(s) => println!("{name}: converged {} it {} E {:.10} F {:.10} S_ent {:.6e} mu {:.8} N {} states {} window [{:.3},{:.3}] integrations {} |vx|/m {:.4} ({:?})", s.converged, s.iterations, s.energies.total, s.energies.free, s.energies.entropy, s.filling.mu, s.energies.n_total, s.spectrum.states.len(), s.window.eps_lo, s.window.eps_hi, s.stats.integrations, s.energies.max_v_x_over_m, start.elapsed()),
            Err(e) => println!("{name}: ERROR {e} ({:?})", start.elapsed()),
        }
    }
}
