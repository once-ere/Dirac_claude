# W8 open items collected from the chapter agents (2026-10-18)

1. Revision record wording `extra_time_modes_grow` (Revision/theory/python/check_field_theory.py line ~857 and
   Revision/docs/DIRAC16COMPLEX_FIELD_THEORY.md line 444): "every extra-time mode eventually enters the growing regime"
   holds only when D = (sin^2 z)^{-1/6} k_x5^2 - tan^2 z k_x0^2 > 0 (the hidden frame momentum grows at the same rate
   e^{H x4/3}); always true without hidden momentum. Textbook chapter 04 (Notebook 04b In [20]) states the limit.
   Fix: qualify the document text (and the check detail if the verifiers are rerun; Notebook 04b quotes record words).
2. Chapter 23 glossary: regenerate with tools/chapter23/run_all.py after all chapters (new bold terms in 02, 04, ...).
3. Notebook 02c's text calls z -> pi - z "the mirror property" (correct, but could be confused with the withdrawn mirror
   copy); reword if 02c is ever rebuilt.
4. Notebooks kept as stored Windows builds although nbkit check differs on Linux at the rounding level: 02a (figure 3),
   02c (figure 3), 02d (four printed rounding-level values in In [9] and In [12]), 13a (one residual 1.8e-12 vs 2.0e-12),
   10a/10c/10d/10e/10g (printed rounding errors; to be confirmed by the chapter-10 agent), 07d (figure 3; chapter-07 agent).
5. 03a kept as built on Windows (figure 03a_5 differs on Linux in 93 of 750,252 pixels by at most 3 levels).
6. 03d: its text could add that the extra-time particle reaches the tip near tau = 2.81 (chapter 03, Exercise 10), so
   that the "turning point predicted by the exact law at tau = 6.877" is never reached inside the half cell; the
   notebook's wording ("would reach", the check "reaches the tip cut-off before any turning point") is correct.
7. Revision/kohn_sham/ks-theory.json (thermodynamics) says mu is fixed by sum w g f = N, while the solver and
   parameters.json (conventions.particleNumber) use sum g f = N; chapters 13 and 14 follow parameters.json and say so.
8. The KS record keeps legacy "brane" names (results/spectrum/brane-band.csv, brane-band-slope.csv, check
   brane_band_slope, key braneBandSlope, parameters.json conventions.brane); the textbook explains them in one
   parenthesis; renaming them would be a Revision record change.
9. Notebook 13a: its printed residuals (~1e-12) vary from run to run in the last digit even on one machine (numpy's
   SIMD reductions depend on the alignment of arrays); kept as stored; chapter 13 says another computer may print
   other last digits.
10. 07d kept as stored (figure 3 differs in 4 pixels by at most 2 levels).
