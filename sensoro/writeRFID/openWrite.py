#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
cgitb.enable()

print("Content-Type: text/plain;charset=utf-8")
print()

exec(open(Write.py).read())
