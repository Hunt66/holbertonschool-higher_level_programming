#!/usr/bin/python3
""" prints body response """
import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as r:
    html = r.read()
    print("Body response:")
    print("    - type: " + str(type(html)))
    print("    - content: " + str(html))
    print("    - utf8 content: " + str(html.decode('utf-8')))
