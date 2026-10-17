#!/bin/bash
# Build the PDFs of Revision/universe_model from their Markdown sources (md2tex.py, then pdflatex twice; every call under
# timeout -k 5 120).  Usage (from the repository root): bash Revision/universe_model/tools/build_pdfs.sh [NAME ...]
# NAME is a document stem (MODEL, PROVENANCE, FIELD_EQUATIONS, SOLUTION); default: every *.md of the folder except README.
set -e
D=Revision/universe_model
names=("$@")
if [ ${#names[@]} -eq 0 ]; then
  for f in $D/*.md; do b=$(basename "$f" .md); [ "$b" = README ] || names+=("$b"); done
fi
mkdir -p build/universe_model
for n in "${names[@]}"; do
  python $D/tools/md2tex.py $D/$n.md $D/$n.tex
  for pass in 1 2; do
    timeout -k 5 120 pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build/universe_model $D/$n.tex > build/universe_model/$n.pdflatex.log 2>&1 || { echo "pdflatex FAILED for $n"; grep -A3 "^!" build/universe_model/$n.log | head -20; exit 1; }
  done
  cp build/universe_model/$n.pdf $D/$n.pdf
  warn=$(grep -c "LaTeX Warning\|Overfull\|Underfull" build/universe_model/$n.log || true)
  pages=$(grep -o "Output written on .* (\([0-9]*\) page" build/universe_model/$n.log | grep -o "([0-9]* page" | tr -d '(' )
  echo "$n.pdf: $pages, warnings/over-/underfull boxes: $warn"
done
