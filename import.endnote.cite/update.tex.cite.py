import csv
import re

def apply_changes(content, changes):
    for original, new in changes:
        escaped_original = re.escape(original)
        content = re.sub(r'\b' + escaped_original + r'\b', new, content)
    return content

def main():
    changes_file = "chg.tsv"
    input_file = "sub.tex"
    output_file = "out.tex"

    changes = []  # To store original and new labels

    with open(changes_file, 'r', newline='', encoding='utf-8') as f:
        tsv_reader = csv.reader(f, delimiter='\t')
        next(tsv_reader)  # Skip header row
        for row in tsv_reader:
            original_label, new_label = row
            changes.append((original_label, new_label))

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    modified_content = apply_changes(content, changes)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(modified_content)

if __name__ == "__main__":
    main()
