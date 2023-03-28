"""
name: wpxz.py
description: Automatically download files on aliyundrive.
author: hdaojin
date: 2023.02.20
update: 2023.02.20
version: 0.0.1
"""

from pathlib import Path

import click
from aligo import Aligo

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('aliy_path', required=True)
@click.argument('local_path', required=True, type=click.Path(exists=True,dir_okay=True,file_okay=False,writable=True), nargs=1)
def main(aliy_path, local_path):
    """
    Automatically download files on aliyundrive.

    ALIY_PATH: The path of the directory on aliyundrive.

    LOCAL_PATH: The path of the directory on local.
    """ 
    ali = Aligo()
    # Get the file object of the directory or file which you want download on aliyundrive.
    file = ali.get_folder_by_path(aliy_path)
    
    if file.type == 'file':
        ali.download_file(file=file, local_folder=local_path)
    else:
        ali.download_folder(file.file_id, local_folder=local_path)

if __name__ == '__main__':
    main()