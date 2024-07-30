# script3_kill_servers.py
import subprocess
import re

def kill_processes_by_name(name):
    """Kill processes by name on Windows."""
    try:
        # Get the list of processes with the given name
        result = subprocess.run(['tasklist'], stdout=subprocess.PIPE, text=True)
        processes = result.stdout.splitlines()

        # Use regex to find process IDs
        for process in processes:
            if name in process:
                # Extract PID from the process line
                match = re.search(r'(\d+)', process)
                if match:
                    pid = match.group(1)
                    # Kill the process by PID
                    subprocess.run(['taskkill', '/PID', pid, '/F'])
                    print(f"Killed process with PID {pid}")
    except Exception as e:
        print(f"Error while killing processes: {e}")

if __name__ == '__main__':
    kill_processes_by_name('jupyter-notebook.exe')
