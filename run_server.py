import os
import shutil
import subprocess
import csv
import time
import secrets
import string

# Paths
template_folder = 'template'
base_path = 'base'
csv_file = 'jupyter_servers.csv'

def generate_token(length=16):
    """Generate a secure random token."""
    return ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length))

# Create user folders and copy contents
user_folders = [f'user{i+1}' for i in range(15)]
for user_folder in user_folders:
    user_path = os.path.join(base_path, user_folder)
    shutil.copytree(template_folder, user_path, dirs_exist_ok=True)

# Store token and server URL in a CSV file
with open(csv_file, 'w', newline='') as csvfile:
    fieldnames = ['User', 'Token', 'URL']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Start Jupyter servers and generate unique tokens
    for i, user_folder in enumerate(user_folders):
        port = 8000 + i
        user_path = os.path.join(base_path, user_folder)
        token = generate_token()  # Generate a unique token for each user

        # Start Jupyter server with unique token
        command = [
            'jupyter', 'notebook',
            '--ip=0.0.0.0',
            '--no-browser',
            '--port={}'.format(port),
            '--NotebookApp.token={}'.format(token),
            '--notebook-dir={}'.format(user_path)
        ]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Wait for the server to start
        time.sleep(10)  # Adjust if needed

        # Form the URL
        url = f'http://localhost:{port}/?token={token}'

        # Write to CSV
        writer.writerow({
            'User': user_folder,
            'Token': token,
            'URL': url
        })

        print(f'Started server for {user_folder} at port {port} with token {token}')

print('Jupyter servers are running, and the CSV file has been created.')
