import toml
import re

with open('hugo.toml', 'r') as file:
    data = toml.load(file)

md_content = '''<img src="../static/images/avatar_small.jpg" alt="drawing" width="160"/>\n\n'''
md_content += '# ' + data['params']['author']
md_content += "\n\n"
md_content += '**' + data['params']['info'] + "**"
md_content += "\n\n"

md_content += "### Contact info\n\n"
for item in data['params']['social']:
    md_content += "- [" + item['name'] + ": " + item['url'].replace('mailto:', '') + "](" + item['url'] + ")\n"
md_content += "\n"

md_content += "### Experience\n\n"
with open('content/about.md', 'r') as file:
    experience_md = file.read()
lines = experience_md.split('\n')
if len(lines) > 5:
    remaining_lines = lines[5:]
else:
    remaining_lines = []
experience_md = '\n'.join(remaining_lines)
image_pattern = r'!\[.*?\]\(.*?\)'
experience_md = re.sub(image_pattern, '', experience_md)
md_content += experience_md

with open('export/vladimirparfenov.md', 'w') as file:
    file.write(md_content)
