import yaml

workflow_file = ".github/workflows/docs-deploy.yml"
changes_made = False

try:
    with open(workflow_file, "r") as f:
        data = yaml.safe_load(f)
except FileNotFoundError:
    print(f"Error: {workflow_file} not found. Will create a new one based on the plan.")
    # Define a base structure if the file is missing, derived from previous attempts
    data = {
        'name': 'Deploy Documentation to GitHub Pages',
        'on': {'push': {'branches': ['**']}},
        'jobs': {
            'deploy': {
                'runs-on': 'ubuntu-latest',
                'permissions': {'contents': 'write'},
                'steps': [
                    {'name': 'Checkout code', 'uses': 'actions/checkout@v4'},
                    {'name': 'Set up Python', 'uses': 'actions/setup-python@v5', 'with': {'python-version': '3.x'}},
                    {'name': 'Install dependencies', 'run': 'python -m pip install --upgrade pip\npip install -r requirements-docs.txt'}, # Assuming requirements-docs.txt is the target
                    {'name': 'Build MkDocs site', 'run': 'mkdocs build'},
                    {'name': 'Deploy to GitHub Pages', 'uses': 'peaceiris/actions-gh-pages@v4', 'with': {
                        'github_token': '${{ secrets.GX_TOKEN }}', # Placeholder, will be set
                        'publish_dir': './site',
                        'user_name': 'github-actions[bot]',
                        'user_email': 'github-actions[bot]@users.noreply.github.com'
                    }}
                ]
            }
        }
    }
    changes_made = True # Since we are creating it

# Ensure top-level permissions for the job
if 'jobs' in data and 'deploy' in data['jobs']:
    if data['jobs']['deploy'].get('permissions', {}).get('contents') != 'write':
        if 'permissions' not in data['jobs']['deploy'] or data['jobs']['deploy']['permissions'] is None:
            data['jobs']['deploy']['permissions'] = {}
        data['jobs']['deploy']['permissions']['contents'] = 'write'
        changes_made = True
else: # Handle case where jobs or deploy key might be missing from a pre-existing malformed file
    print("Warning: 'jobs.deploy' structure not found or incomplete. Rebuilding deploy job structure.")
    data['jobs'] = data.get('jobs', {})
    data['jobs']['deploy'] = data['jobs'].get('deploy', {}) # Ensure deploy key exists
    if not isinstance(data['jobs']['deploy'], dict): data['jobs']['deploy'] = {} # Ensure deploy value is a dict
    data['jobs']['deploy']['permissions'] = {'contents': 'write'}
    # Add other necessary fields if they are missing, based on a standard template
    if 'runs-on' not in data['jobs']['deploy']: data['jobs']['deploy']['runs-on'] = 'ubuntu-latest'
    if 'steps' not in data['jobs']['deploy']: data['jobs']['deploy']['steps'] = [ # Add default steps if missing
        {'name': 'Checkout code', 'uses': 'actions/checkout@v4'},
        {'name': 'Set up Python', 'uses': 'actions/setup-python@v5', 'with': {'python-version': '3.x'}},
        {'name': 'Install dependencies', 'run': 'python -m pip install --upgrade pip\npip install -r requirements-docs.txt'},
        {'name': 'Build MkDocs site', 'run': 'mkdocs build'},
        {'name': 'Deploy to GitHub Pages', 'uses': 'peaceiris/actions-gh-pages@v4', 'with': {
            'github_token': '${{ secrets.GX_TOKEN }}',
            'publish_dir': './site',
            'user_name': 'github-actions[bot]',
            'user_email': 'github-actions[bot]@users.noreply.github.com'
        }}
    ]
    changes_made = True


# Ensure trigger is set for all branches
# Ensure 'on' and 'on.push' are dictionaries before accessing 'branches'
if not isinstance(data.get('on'), dict): data['on'] = {}
if not isinstance(data['on'].get('push'), dict): data['on']['push'] = {}
if data['on']['push'].get('branches') != ['**']:
    data['on']['push']['branches'] = ['**']
    changes_made = True

# Update peaceiris/actions-gh-pages step
deploy_step_found = False
if 'jobs' in data and isinstance(data['jobs'], dict) and \
   'deploy' in data['jobs'] and isinstance(data['jobs']['deploy'], dict) and \
   'steps' in data['jobs']['deploy'] and isinstance(data['jobs']['deploy']['steps'], list):
    for step in data['jobs']['deploy']['steps']:
        if isinstance(step, dict) and step.get('uses') and 'peaceiris/actions-gh-pages' in step.get('uses', ''):
            deploy_step_found = True
            if 'with' not in step or step['with'] is None or not isinstance(step['with'], dict): # Ensure 'with' key exists and is a dict
                step['with'] = {}
                changes_made = True

            if step['with'].get('github_token') != '${{ secrets.GX_TOKEN }}':
                step['with']['github_token'] = '${{ secrets.GX_TOKEN }}'
                changes_made = True
            if step['with'].get('user_name') != 'github-actions[bot]':
                step['with']['user_name'] = 'github-actions[bot]'
                changes_made = True
            if step['with'].get('user_email') != 'github-actions[bot]@users.noreply.github.com':
                step['with']['user_email'] = 'github-actions[bot]@users.noreply.github.com'
                changes_made = True
            if step['with'].get('publish_dir') != './site': # Ensure publish_dir is there and correct
                 step['with']['publish_dir'] = './site'
                 changes_made = True
            break
    if not deploy_step_found:
        print("Warning: peaceiris/actions-gh-pages step not found. Adding it.")
        # Add the step if it's missing
        data['jobs']['deploy']['steps'].append({
            'name': 'Deploy to GitHub Pages',
            'uses': 'peaceiris/actions-gh-pages@v4',
            'with': {
                'github_token': '${{ secrets.GX_TOKEN }}',
                'publish_dir': './site',
                'user_name': 'github-actions[bot]',
                'user_email': 'github-actions[bot]@users.noreply.github.com'
            }
        })
        changes_made = True
else:
    print("Warning: 'jobs.deploy.steps' structure not found or invalid. Cannot configure deployment step effectively.")


if changes_made:
    with open(workflow_file, "w") as f:
        yaml.dump(data, f, sort_keys=False, default_flow_style=False, width=1000) # Added flow and width for better formatting
    print(f"INFO: {workflow_file} updated.")
else:
    print(f"INFO: {workflow_file} already configured as per plan.")

# Print content for verification
with open(workflow_file, "r") as f:
    print(f"\nContent of {workflow_file}:")
    print(f.read())
