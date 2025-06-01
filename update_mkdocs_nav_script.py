import yaml

# 1. Read mkdocs.yml
with open("mkdocs.yml", "r") as f:
    config = yaml.safe_load(f)

# 2. (Already parsed by safe_load)

# 3. Add to nav
# Ensure 'nav' exists and is a list
if 'nav' not in config or not isinstance(config['nav'], list):
    config['nav'] = [] # Initialize or reset if structure is not as expected

# Find insertion index (e.g., after 'Features' or at the end if 'Features' not found)
# Current nav:
# - Home: index.md
# - Commands: COMMANDS.md
# - Configurations: CONFIGURATIONS.md
# - Deployment: DEPLOYMENT.md
# - Features: FEATURES.md
# - Extras: EXTRAS.md

new_nav_item = {"Task Options": "TASK_OPTIONS.md"}
inserted = False
for i, item in enumerate(config['nav']):
    if isinstance(item, dict) and "Features" in item:
        config['nav'].insert(i + 1, new_nav_item)
        inserted = True
        break
if not inserted: # If 'Features' wasn't found or nav was empty
    config['nav'].append(new_nav_item)

# 4. Write updated YAML back
with open("mkdocs.yml", "w") as f:
    yaml.dump(config, f, sort_keys=False) # sort_keys=False to preserve order

# 5. Print nav section
with open("mkdocs.yml", "r") as f:
    updated_config_str = f.read()
    print("Updated mkdocs.yml content:")
    print(updated_config_str)
    # For more specific printing if needed:
    # final_config = yaml.safe_load(updated_config_str)
    # if 'nav' in final_config:
    # print("\nNav section only:")
    # print(yaml.dump({'nav': final_config['nav']}, sort_keys=False))
