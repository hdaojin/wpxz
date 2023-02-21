"""
Name: wptb.py
Description: Automatically sync files between aliyundrive and local.
Author: hdaojin
Date: 2023.02.20
Update: 2023.02.21
Version: 0.0.1
"""

from pathlib import Path
import logging

from aligo import Aligo

def sync_files(local_path, aliy_path):
    # Create local directory if it does not exist.
    if isinstance(local_path, str):
        local_path = Path(local_path)
    if not local_path.exists():
        local_path.mkdir(parents=True)

    # Get the file_id of the directory on aliyundrive.
    aliy_folder_id = ali.get_folder_by_path(aliy_path).file_id

    try:
        # Sync files between local and aliyundrive. `False` means clould-base.
        ali.sync_folder(local_path, aliy_folder_id, False)
    except Exception as e:
        logging.basicConfig(filename='wptb.log', encoding='utf-8', level=logging.ERROR)
        logging.error(e)


if __name__ == '__main__':
    ali = Aligo()
    # Sync files between 'Offline' directory on aliyundrive and local.
    local_path = Path.home() / 'Downloads'
    aliy_path = 'Offline'
    sync_files(local_path, aliy_path)