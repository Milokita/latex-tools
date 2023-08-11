import re

def add_RN_to_citations(text):
    def repl(match):
        citations = match.group(1)
        citations = re.sub(r'\b(?<!RN)(\d+)\b', r'RN\1', citations)
        return f'\\cite{{{citations}}}'

    pattern = r'\\cite\{([^\}]*)\}'
    modified_text = re.sub(pattern, repl, text)
    return modified_text

# Read the input TeX file
input_tex_file_path = 'in.tex'
with open(input_tex_file_path, 'r') as tex_file:
    tex_content = tex_file.read()

# Process and modify the content
modified_tex_content = add_RN_to_citations(tex_content)

# Write the modified content to the output TeX file
output_tex_file_path = 'sub.tex'
with open(output_tex_file_path, 'w') as modified_tex_file:
    modified_tex_file.write(modified_tex_content)
