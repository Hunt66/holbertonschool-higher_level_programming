#!/usr/bin/python3
""" takes URL and an email and sends POST reques to the URL with email
    peramiter, then dsplys body respose"""
import urllib.request
import urllib.parse
import sys

if len(sys.argv) < 2:
    print("requires URL and email")
elif len(sys.argv) < 3:
    print("requires email")
else:
    stf = urllib.parse.urlencode({'email' : sys.argv[2]}).encode('utf-8')
    with urllib.request.urlopen(sys.argv[1], stf) as r:
        print(r.read().decode('utf-8'))
