#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/home/pi/bigBrother/sensoro/writeRFID')
# enable debugging
import cgitb

cgitb.enable()

print("Content-Type: text/plain;charset=utf-8")
print()

exec(open("Write.py").read())
