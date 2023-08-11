# Adapt the endnote cite to latex

  since the citations exported from docx is "/cite{RN1,2,3}" cause confusion and collisions with existing cites, this code addresses this problem. 

# Requirement

1. python package bibtexparser
   
   ``` pip install bibtexparser ```

2. tex file copied from docx, must be named as "in.tex"

3. bib citation file export from Endnote, must be named as "in.bib"

# How to use

Simply run the code below

  ``` bash run.sh ```

# Workflow

1. convert all "/cite{RN1,2,3}" to "/cite{RN1,RN2,RN3}"

2. update the label of exported bib according to the "author", "first 5 characters of title" and "year" and update the change table (chg.tsv) for the corresponding change.

3. substitute all the old "RN" labels according to the change label
