#!/usr/bin/python3
""" takes a URL sends request and displays the value of X-Request-Id found in
     the header """

import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as r:
    print(r.info()['X-Reqest-Id'])
