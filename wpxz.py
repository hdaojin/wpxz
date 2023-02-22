"""
name: wpxz.py
description: Automatically update and download files shared on aliyundrive.
author: hdaojin
date: 2023.02.20
update: 2023.02.20
version: 0.0.1
"""

from pathlib import Path
import logging

from aligo import Aligo

def get_folder_list(base_folder):
    folder_list = ali.get_file_list(ali.get_folder_by_path(base_folder).file_id)
    return folder_list

def download_files(file_list, local_path):
    if isinstance(local_path, str):
        local_path = Path(local_path)
    if not local_path.exists():
        local_path.mkdir(parents=True)
     
    ali.download_files(files=file_list, local_folder=local_path)

def save_log():
    logging.basicConfig(filename='wpxz.log',
                        filemode='w', 
                        encoding='utf-8', 
                        format='%(asctime)s - %(module)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    ali = Aligo()
    save_log()
    # Get folder list under 'Offline-test' directory on aliyundrive.
    folder_list = get_folder_list('Offline-test')
    for folder in folder_list:
        if folder.type == 'folder':
            folder_id = folder.file_id
            folder_name = folder.name
            file_list = ali.get_file_list(folder_id)
            local_path = Path.home() / 'Downloads' / folder_name
            print(file_list)
            download_files(file_list, local_path)