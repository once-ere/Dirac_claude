# Frozen input of the withdrawn metric of 2026-10-14 (dark sector)

`eos-theory-b4.json` is `Revision/dark_sector/dirac16complex00/eos-theory.json` as committed before phase W6 of the
corrected metric (last changed in commit 1d77417; sha256
7ab0fcbd8bd4fdc39be91b8fa39ff76c83715e7bdd08b8326eb9809249ecd2ac). It is the implementation-A record of
dirac16complex00 for the metric of 2026-10-14 (the metric with b4(x4) and the sin^{1/3} z factors on 3-space), which
the corrected metric of 2026-10-16 replaced.

It is read only by `Revision/dark_sector/wolfram/verify_dark_sector_b4.wls` (gate step dark-b4-wolfram), the
Wolfram verification of that withdrawn record, which is kept so that the record of the withdrawn metric stays
reproducible. The current dark-sector record is in `../dirac16complex00/` and is verified by
`../wolfram/verify_dark_sector.wls` (gate step dark-wolfram).
