"""Replace the body of section 23.17 Glossary in chapter 23 with glossary.md."""
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[4]  # the repository (tools/chapter23 -> tools -> textbook -> Revision -> root)

HERE = Path(__file__).resolve().parent
WORK = ROOT / "build" / "chapter23"  # intermediate files (git-ignored)
WORK.mkdir(parents=True, exist_ok=True)
CH = Path(sys.argv[1]) if len(sys.argv) > 1 else (
    ROOT / "Revision/textbook/chapters/23-reproducing-everything.md")
INTRO = (
    "This glossary lists, in alphabetical order, the technical words that the book "
    "defines: the words printed in bold where a chapter first explains them, the words of "
    "section 3, \"The words used in this notebook\", of every notebook, the words of "
    "the lists \"The words of this chapter\", and a few words that a notebook defines "
    "elsewhere, such as Sakharov's three conditions. Each entry gives the meaning in "
    "plain words, taken from a place that defines the word, and then, in brackets, every "
    "section where the word is defined or explained. A section titled \"Notebook NNx: "
    "complete text\" means section 3 of that notebook; \"the opening of Chapter N\" "
    "means the paragraphs before its first section. Where a word is defined in several "
    "places, the entry quotes the first of them that has the form of a definition (a list "
    "entry \"word: meaning\", or a sentence such as \"a word is ...\"); the other "
    "sections listed explain the same word again, often for a particular case. For a few "
    "central words (among them the five status labels, the extra times, the U(1) charge "
    "and the word universe) the entry is written from all its defining sections. A word "
    "that is defined together with others in one bold phrase (for example \"Eigenvalue, "
    "eigenvector\") is listed under that phrase when it has no entry of its own. The "
    "words in capitals PROVED, COMPUTED, ASSUMED, HYPOTHESIS and OPEN are the five status "
    "labels of the book; each has its own entry.\n"
)
text = CH.read_text(encoding="utf-8")
head = "### 23.17 Glossary\n"
i = text.find(head)
if i < 0 or text.count(head) != 1:
    sys.exit("glossary heading not found exactly once")
rest = text[i + len(head):]
if "\n### " in rest:
    sys.exit("a section follows the glossary; refusing")
body = (WORK / "glossary.md").read_text(encoding="utf-8")
new = text[:i] + head + "\n" + INTRO + "\n" + body
CH.write_bytes(new.encode("utf-8"))
print("old glossary body:", repr(rest[:80]), "new length", len(new))
