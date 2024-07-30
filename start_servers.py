# script2_start_servers.py
import os
import subprocess
import csv
import time
import secrets
import string

# Paths
base_path = 'base'
csv_file = 'jupyter_servers.csv'

def generate_token(length=16):
    """Generate a secure random token."""
    return ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length))

# Start Jupyter servers and generate unique tokens
with open(csv_file, 'w', newline='') as csvfile:
    fieldnames = ['User', 'Token', 'URL']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    user_folders = [f'user{i+1}' for i in range(4)]
    for i, user_folder in enumerate(user_folders):
        port = 8000 + i
        user_path = os.path.join(base_path, user_folder)
        token = generate_token()  # Generate a unique token for each user

        # Start Jupyter server with unique token
        command = [
            'jupyter', 'notebook',
            '--ip=192.168.137.1',
            '--no-browser',
            '--port={}'.format(port),
            '--NotebookApp.token={}'.format(token),
            '--notebook-dir={}'.format(user_path)
        ]

        # Start the process
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Wait for the server to start
        time.sleep(10)  # Adjust if needed

        # Output the logs to the console
        print(f'Starting server for {user_folder} at port {port}...')
        # while True:
        #     output = process.stdout.readline()
        #     if output == '' and process.poll() is not None:
        #         break
        #     if output:
        #         print(f'{user_folder} (port {port}): {output.strip()}')
        
        # Wait a bit to ensure the server is fully started
        time.sleep(2)

        # Form the URL
        url = f'http://192.168.137.1:{port}/?token={token}'

        # Write to CSV
        writer.writerow({
            'User': user_folder,
            'Token': token,
            'URL': url
        })

        print(f'Started server for {user_folder} at port {port} with token {token}')

print('Jupyter servers are running, and the CSV file has been created.')
