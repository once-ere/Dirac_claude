# Relabel tools: the author's coordinates x0..x7 and the metric with b4

These are the scripts that were used on 2026-10-14 to move chapters 00 to 06 of the textbook
"Universes in Pairs" (chapters, notebook builders, notebooks, figures) to two things:

* the author's coordinates $\{x0, x1, \dots, x7\}$;
* the metric with $b_4(x_4)$ (Revision/metric_b4/METRIC_CHANGE_PROVENANCE.md).

Chapters 07 to 23 still use the old labels. HANDOFF.md, section 0.6, lists what remains.

The coordinates:

* x0 is the hidden direction ($z = 6Hx_0$) and comes FIRST;
* x1, x2, x3 are 3-space, x4 is the time, x5, x6, x7 are the extra times;
* Python index k is xk, and $\gamma^{(xk)}$ is the author's `T16[k]` (`T16[8]` is $\Gamma$);
* the Revision record files number the directions from 1 in the order x0..x7, so subtract 1.

Never write x8, $x_1..x_8$, `gamma[7]` for the hidden direction, or the old order with the hidden direction last.

Every script is run from the repository folder with `python -X utf8 Revision/textbook/tools/relabel/<script> ...`.
None of them takes more than a few seconds.

| Script | What it does | Usage |
|---|---|---|
| `tb_relabel.py` | Does the mechanical part of the relabel. Enumerations 1..8 become 0..7, fixed lists in the old order become the author's order, and every remaining label of the hidden direction 8 becomes 0. It does NOT fix code that indexes arrays by position: such lines are listed for a manual review. | `tb_relabel.py FILE... [--dry]` |
| `relabel_common.py` | Holds the shared helpers. `strict_replace(text, pairs, label)` replaces each old string, which must occur exactly once (or a given count), and stops on any miss. `NAME_MAP` holds the renamed check names; `relabel_code_spans` and `leftovers` are also here. | imported |
| `scan_old.py` | Counts the old labels left in textbook files; `--lines` lists them. False positives: `M8`/`w8` (an 8x8 matrix, an 8-vector) in 01e, and `axvspan`/`axhspan` in 05f. | `scan_old.py FILE... [--lines]` |
| `risk_scan.py` | Flags lines that may still use the old numbering 1..8 or the old order. Read each flagged line; most are correct (e.g. `eta = diag(+1,+1,+1,+1,-1,-1,-1,-1)` IS the x0..x7 order). | `risk_scan.py FILE...` |
| `wt_remap.py` | After a notebook is rebuilt, re-maps the quoted ```python blocks of a chapter's walk-through to the new cells, using the HEAD notebook as the old reference. Run it BEFORE committing the rebuilt notebook. | `wt_remap.py CHAPTER NB_ID [--dry]` |
| `wt_contiguous.py` | Reports the walk-through blocks whose lines are not one contiguous run of their notebook cell (a fuzzy re-mapping can misplace a line). Run it after `wt_remap.py`; it must report 0. | `wt_contiguous.py CHAPTER NB_ID` |
| `wt_fill.py` | Lists, or appends, the cell lines that follow a block directly and that no block quotes. Use `--dry` and apply only genuine gaps: the walk-throughs leave plotting code out ON PURPOSE. | `wt_fill.py CHAPTER NB_ID [--dry]` |
| `wrap_long.py` | Wraps the builder source lines longer than 93 characters (cell lines may have at most 89 after the 4-space dedent); a string literal is split into two. | `wrap_long.py BUILDER.py` |
| `prose_indices.py` | Lists the prose lines (outside code blocks) that quote code with a literal index or range, such as `gamma[3]`, `T[3, 0]` or `range(4, 7)`. These descriptions must follow the new positions. | `prose_indices.py CHAPTER` |
| `check_all.py` | Runs `nbkit.py check` (re-execution, byte-for-byte comparison; the repository is not changed) for every builder of the given chapters, 8 at a time, each with a hard limit of 423 s, and writes one line per notebook: status, seconds, first problem. Use it to see which notebooks still fail against the relabelled records. | `check_all.py OUT.tsv 10 11 12` |
| `nb_outputs.py` | Prints every code cell's text output of a notebook (for RESULT lines and counts). | `nb_outputs.py NB.ipynb` |
| `nb_out_diff.py` | Shows the output lines of rebuilt notebooks that changed against HEAD. | `nb_out_diff.py 06a 06b` |
| `prov_hashes.py` | Checks the sha256 and size of every file in the "writes" tables of the notebook PROVENANCE files. | `prov_hashes.py 05 06` |
| `prose.py` | Prints a chapter with its code blocks collapsed, with line numbers, for reading the prose. | `prose.py CHAPTER [FROM] [TO]` |
| `splice.py` | Replaces the text between two markers (start inclusive, end exclusive) with the content of a file. | `splice.py TARGET START END NEWFILE` |

`examples/` holds four of the chapter 06 fix scripts as models. Each is a list of (old, new) pairs applied with `strict_replace`. They have already been applied, so running them again stops at once ("not found").

**Warning.** On this machine a bash heredoc can turn `\\` into `\`, and Python then reads `\f` in `\frac` as a form feed. Write every edit script with an editor or a file-writing tool, never as a heredoc. After every edit, check that no source file contains a control character.

**Random numbers.** Some builders draw numbers indexed by direction, such as `rng.normal(size=(8, 16))`. To keep every printed number of the first edition, draw them in the old way and reorder the rows (`np.roll(table, 1, axis=0)` moves the old last row, x8, to the front as x0), and say so in the walk-through (09a does this).

## The procedure per chapter (as done for chapters 03 to 09)

1. **Builders.** Run `tb_relabel.py` on `Revision/textbook/notebooks/src/NNx_*.py`, then fix every listed position by hand:
   * hidden direction at index 0, time at index 4;
   * `range(1, 4)` for 3-space and `range(5, 8)` for the extra times;
   * record keys minus 1.

   Where the notebook reads a record that changed with b4, compare with both the b4 record and the b4 = 1 record. Use a helper `at_b4_1` (`expr.subs(b4, 1).doit()`): sympy leaves `Derivative(1, x4)` otherwise.
2. **Rebuild** each notebook:

   ```
   timeout 423 python -B Revision/textbook/tools/nbkit.py build Revision/textbook/notebooks/src/NNx_name.py --date YYYY-MM-DD --scratch <scratch dir>
   ```

   Lines must be at most 89 characters. In matplotlib labels, write `\frac{3}{4}`, not `\frac34`. Never wait more than 423 s for one build.
3. **Chapter.** Run `tb_relabel.py` on the chapter and `wt_remap.py CHAPTER NNx` for each notebook. Then rewrite the prose that states metric-dependent results with b4: the vielbein, `sqrt|g|`, the rates, `gamma^mu Omega_mu`, the Ricci tensor, and the rescaling. Use `strict_replace` scripts.
4. **Verify:**
   * `Revision/textbook/tools/audit/walkthrough_diff.py CHAPTER NB.ipynb NNx` for each notebook;
   * `scan_old.py` and `risk_scan.py`;
   * `prov_hashes.py NN`;
   * the assembly:

     ```
     python Revision/textbook/tools/assemble_textbook.py --only 00 ... NN --allow-missing --output <scratch>/draft.md
     ```
5. **Commit** the specific paths only (never the author's notebook `Dirac_Einstein-Lovelock_4+4_Nash.nb`), then push.
