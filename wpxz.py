"""
name: wpxz.py
description: Automatically update and download files shared on aliyundrive.
author: hdaojin
date: 2023.02.20
update: 2023.02.20
version: 0.0.1
"""

from pathlib import Path

from aligo import Aligo

def get_file_list(aly_path):
    file_list = ali.get_file_list(aly_path)
    all_files_name = []
    for file in file_list:
        if file.type == 'file':
            all_files_name.append(file.name)

def download_file(files, local_path):
    if isinstance(local_path, str):
        local_path = Path(local_path)
    if not local_path.exists():
        local_path.mkdir(parents=True)

    ali.download_files(files=files, local_folder=local_path)

    # if file.type == 'file':
    #     ali.download_file(file=file, local_folder=local_path)
    # else:
    #     ali.download_folder(file.file_id, local_folder=local_path)

if __name__ == '__main__':
    ali = Aligo()
    files = get_file_list('电视剧/海贼王')
    download_file(files, '/home/demo/Downloads/海贼王')