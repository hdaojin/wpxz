#!/bin/bash

source_dir="/home/pi/GitHub/hdaojin/wpxz"

source $source_dir/.venv/bin/activate  &&  python3 $source_dir/aliy_signin.py

sleep 10

sudo python3 $source_dir/aliy_download.py  Offline  /usb_disk1/
