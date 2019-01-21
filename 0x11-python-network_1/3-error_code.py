#!/usr/bin/python3
""" sends request to the URL and displays the body response"""

import urllib.request
import urllib.parse
import urllib.error
import sys


if len(sys.argv) < 2:
    print("need argument")
else:
    try:
        with urllib.request.urlopen(sys.argv[1]) as r:
            print(r.read().decode('utf-8'))
    except urllib.error.HTTPError as err:
        print("Error code: " + str(err.code))
