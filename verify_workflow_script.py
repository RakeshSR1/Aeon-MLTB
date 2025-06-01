import yaml

workflow_file = ".github/workflows/docs-deploy.yml"
changes_made = False

try:
    with open(workflow_file, "r") as f:
        data = yaml.safe_load(f)
except FileNotFoundError:
    print(f"Error: {workflow_file} not found. Cannot apply changes.")
    # If the file doesn't exist, we might need to recreate it from the earlier plan step.
    # For now, this subtask will report failure.
    exit(1)


# Ensure permissions are set
if 'jobs' in data and 'deploy' in data['jobs']:
    if data['jobs']['deploy'].get('permissions', {}).get('contents') != 'write':
        if 'permissions' not in data['jobs']['deploy'] or data['jobs']['deploy']['permissions'] is None:
            data['jobs']['deploy']['permissions'] = {}
        data['jobs']['deploy']['permissions']['contents'] = 'write'
        changes_made = True
else:
    print("Warning: 'jobs.deploy' structure not found in workflow file. Cannot set permissions.")


# Ensure trigger is set for all branches
if 'on' in data and isinstance(data['on'], dict) and 'push' in data['on'] and isinstance(data['on']['push'], dict):
    if data['on']['push'].get('branches') != ['**']:
        data['on']['push']['branches'] = ['**']
        changes_made = True
elif 'on' in data and isinstance(data['on'], dict) : # if 'on' exists but not 'push' or 'push' is not a dict
    data['on']['push'] = {'branches': ['**']} # default to this structure
    changes_made = True
else: # if 'on' does not exist or is not a dictionary
    data['on'] = {'push': {'branches': ['**']}}
    changes_made = True


if changes_made:
    with open(workflow_file, "w") as f:
        yaml.dump(data, f, sort_keys=False)
    print(f"{workflow_file} updated.")
else:
    print(f"{workflow_file} already has the correct permissions and trigger.")

# Print content for verification
with open(workflow_file, "r") as f:
    print("\nContent of .github/workflows/docs-deploy.yml:")
    print(f.read())
