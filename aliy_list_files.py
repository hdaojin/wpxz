"""
Name: aliy_list_files.py
Description: List directroy and files on aliyundrive.
Author: hdaojin
Date: 2023.03.26
Update: 2023.03.26
Version: 0.0.1
"""

from aligo import Aligo

if __name__=='__main__':
    ali = Aligo()
    ll = ali.get_file_list()
    for f in ll:
        print(f.name, f.type, f.file_id, f.size, f.parent_file_id, )