## 23. Reproducing everything

This chapter is a PLACEHOLDER. It was planned (TEXTBOOK_SPEC section 5, chapter 23) but has not been written yet. The book was assembled on 2026-10-08 with this placeholder so that the whole book can be read and built now. Every statement in this placeholder is a plan, not a result.

### 23.1 What this chapter will contain

The finished chapter will contain the following parts.

- Every command that reproduces the book: the Revision verifiers and checkers, every notebook of the book, and the PDF build.
- Notebook 23a, which runs every notebook of the book headless with the check mode of nbkit and shows a table and a timing bar chart.
- The glossary of the book.
- The index of the checks and of the notebooks.

### 23.2 What you can do now

Each notebook of this book already carries its own complete run instructions, printed in the section "How to run Notebook NNx" just before the notebook's text. Each notebook also has a provenance file `X.PROVENANCE.md` next to it in `Revision/textbook/notebooks/`. To re-run one notebook headless and compare it byte for byte with the stored copy, run these commands from the repository root:

```text
cd Revision/textbook
python tools/nbkit.py --check notebooks/src/<builder>.py
```

The verifiers and checkers of the Revision record are listed, with their run instructions, in the `WOLFRAMSCRIPT_PROVENANCE.md` files next to each Wolfram set under `Revision/`.
