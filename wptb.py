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

import click
from aligo import Aligo

def sync_files(local_path, aliy_path):
    # Get the file_id of the directory on aliyundrive.
    try:
        aliy_folder_id = ali.get_folder_by_path(aliy_path).file_id
    except Exception as e:
        logging.error(e)
        return

    # Sync files between local and aliyundrive. `False` means clould-base; `True` means local-base; `None` means two-way sync.
    ali.sync_folder(local_path, aliy_folder_id, False)

def save_log():
    logging.basicConfig(filename='wptb.log',
                        filemode='w', 
                        encoding='utf-8', 
                        format='%(asctime)s - %(module)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('aliy_path', required=True)
@click.argument('local_path', required=True, type=click.Path(exists=True,dir_okay=True,file_okay=False,writable=True), nargs=1)
def main(local_path, aliy_path):
    """
    Automatically sync files between aliyundrive and local.

    ALIY_PATH: The path of the directory on aliyundrive.
    LOCAL_PATH: The path of the directory on local.
    """
    sync_files(local_path, aliy_path)
    

if __name__ == '__main__':
    ali = Aligo()
    save_log()
    main()
