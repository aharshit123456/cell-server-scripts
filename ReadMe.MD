# ReadMe for Jupyter Server Management Scripts

## Overview

This repository contains a set of Python scripts for managing Jupyter Notebook servers across multiple user directories. The scripts perform the following tasks:

1. **Sync Folders**: Synchronize user directories with a template directory.
2. **Start Servers**: Start Jupyter Notebook servers for each user and generate unique access tokens.
3. **Kill Servers**: Terminate running Jupyter Notebook servers.

## Requirements

- Python 3.x
- Jupyter Notebook installed (`jupyter` command available in your PATH)
- Administrative privileges for killing processes on Windows

## Script Details

### 1. `handle_files.py`

**Purpose**: Synchronizes user directories with a template directory.

**Usage**:

1. Ensure the `template` folder contains the desired files and subdirectories.
2. Place the script in the same directory as the `template` and `base` folders.
3. Run the script:

   ```bash
   python shandle_files.py
   ```

   **What it does**:

   - Copies files and subdirectories from `template` to each user directory in `base` (e.g., `user1`, `user2`, ..., `user15`).
   - If a user directory already exists, only new and modified files are copied.

### 2. `start_servers.py`

**Purpose**: Starts Jupyter Notebook servers for a predefined list of users and generates access tokens.

**Usage**:

1. Ensure you have the `jupyter` command available and accessible from your PATH.
2. Create a `jupyter_servers.csv` file in the same directory as the script.
3. Place the script in the same directory as the `base` folder.
4. Run the script:

   ```bash
   python start_servers.py
   ```

   **What it does**:

   - Starts a Jupyter Notebook server for each user directory (e.g., `user1`, `user2`, `user3`, `user4`).
   - Generates a unique token for each server and writes the user, token, and URL to `jupyter_servers.csv`.
   - Adjust the `base_path` and port numbers if needed.

### 3. `kill_servers.py`

**Purpose**: Terminates running Jupyter Notebook servers.

**Usage**:

1. Ensure you have administrative privileges if running on Windows.
2. Run the script:

   ```bash
   python kill_servers.py
   ```

   **What it does**:

   - Searches for running `jupyter-notebook.exe` processes and terminates them.
   - Useful for cleaning up servers that are no longer needed.

## Notes

- **Port Conflicts**: The `start_servers.py` script starts servers on ports 8000 through 8003. Adjust port numbers if these ports are in use or if more servers are needed.
- **Token Security**: Each server is started with a unique token. Ensure tokens are kept secure and not shared publicly.
- **Administrative Rights**: `kill_servers.py` may require administrative privileges to terminate processes on Windows.

## Troubleshooting

- **Permission Errors**: Ensure you have the necessary permissions for file operations and process management.
- **Process Not Starting**: Check the output of the `jupyter` command for errors and ensure all dependencies are installed correctly.

## Contributing

Feel free to fork the repository and submit pull requests for improvements or bug fixes. Ensure that your contributions are well-tested and documented.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

For further questions or issues, please contact the repository maintainer or open an issue on the project's GitHub page.
