#!/usr/bin/python3
"""   """
import requests
import sys


if len(sys.argv) < 2:
    print("requires URL")
else:
    r = requests.get(sys.argv[1])
    print(r.headers['X-Request-Id'])
