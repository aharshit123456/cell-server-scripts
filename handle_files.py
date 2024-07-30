# script1_sync_folders.py
import os
import shutil
from filecmp import dircmp

# Paths
template_folder = 'template'
base_path = 'base'

def sync_directories(src, dst):
    """Sync the contents of src directory to dst directory."""
    if not os.path.exists(dst):
        shutil.copytree(src, dst)
        print(f"Copied from {src} to {dst}")
    else:
        dcmp = dircmp(src, dst)
        print(f"Comparing {src} and {dst}")
        # print(dcmp.right_only)
        # Copy new and modified files
        for name in dcmp.left_only:
            src_path = os.path.join(src, name)
            dst_path = os.path.join(dst, name)
            print(f"Copying new file {name} to {dst}")
            shutil.copy2(src_path, dst_path)
            print(f"Copied new file {name} to {dst}")

        # Recursively sync subdirectories
        for sub_dir in dcmp.common_dirs:
            sync_directories(os.path.join(src, sub_dir), os.path.join(dst, sub_dir))

if __name__ == '__main__':
    user_folders = [f'user{i+1}' for i in range(15)]
    for user_folder in user_folders:
        user_path = os.path.join(base_path, user_folder)
        sync_directories(template_folder, user_path)
