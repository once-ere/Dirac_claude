//! TEMPORARY diagnostic (not part of the deliverable): the T = 0 fallback of
//! solve_ground at m = 1, L = 3, N = 1016, lambda_hat given.
use dirac16complex_kohn_sham::scf::{solve_ground, standard_params};
fn main() {
    let lh: f64 = std::env::args().nth(1).unwrap().parse().unwrap();
    let refined = std::env::args().nth(2).is_some_and(|a| a == "refined");
    let mut p = standard_params(1.0, 3.0, lh, 0.0, 1016.0);
    if refined {
        p.tolerances.rtol /= 10.0;
        p.tolerances.atol /= 10.0;
        p.tolerances.max_step /= 2.0;
    }
    let s = solve_ground(&p, None, 0.0).unwrap();
    eprintln!(
        "RESULT lh {lh} refined {refined}: converged {} stage {} iterations {} smearing {} beta {} E {:.12} mu {:.12} gap {:?}",
        s.converged, s.params.fallback_stage, s.iterations, s.params.smearing, s.params.mix_beta, s.energies.total, s.filling.mu, s.gap()
    );
}
