#!/usr/bin/python3
""" takes URL and sends a request to display the body response """
import sys
import requests


if len(sys.argv) < 2:
    print("needs URL and email")
else:
    r = requests.get(argv[1])
