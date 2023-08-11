#! /bin/bash

python3 substitue.endnote.cite.py
python3 change.bib.lbl.py
python3 update.tex.cite.py

rm sub.tex
rm chg.tsv