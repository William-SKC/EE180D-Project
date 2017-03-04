#!/bin/bash


FILENAME= "scan_result.txt"

iwlist wlan0 scan | grep 'Address:\|Signal' | sed 's/.*Address: //; s/.*\([0-9]\{2\}\) dBm/\1/' | sed 'N; s/\n/ /' | sort > test_result.txt

python Loc_wifi.py
