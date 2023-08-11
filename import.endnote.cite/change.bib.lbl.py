import bibtexparser

# Read input BIB file
with open('in.bib', 'r', encoding='utf-8') as f:
    bib_database = bibtexparser.load(f)

# Process and update entries
changed_entries = []

for entry in bib_database.entries:
    if 'author' in entry and 'title' in entry and 'year' in entry:
        author = entry['author'].split(' ')[0].lower()  # Use the first author's last name
        title = entry['title'][:5].lower()
        year = entry['year']
        
        # Remove commas and spaces from the labels
        author = author.replace(',', '').replace(' ', '_')
        title = title.replace(',', '').replace(' ', '_')
        
        new_label = f"{author}_{title}_{year}"
        changed_entries.append((entry['ID'], new_label))
        entry['ID'] = new_label

# Save changes to output BIB file
with open('out.bib', 'w', encoding='utf-8') as f:
    bibtexparser.dump(bib_database, f)

# Save changes to TSV file
with open('chg.tsv', 'w', encoding='utf-8') as f:
    f.write("Original Label\tNew Label\n")
    for original_label, new_label in changed_entries:
        f.write(f"{original_label}\t{new_label}\n")

print("Processing completed. Changes saved to out.bib and chg.tsv.")
