import toml
import sys

file_path = "hugo.toml"

# Read the TOML file
with open(file_path, 'r') as file:
    data = toml.load(file)

# Update the value
for item in data['menu']['main']:
    if 'url' not in item:
        item['url'] = "https://api.github.com/repos/ParfenovVS/personal-website/actions/artifacts/" + sys.argv[1]
        break

# Write the changes back to the file
with open(file_path, 'w') as file:
    toml.dump(data, file)
