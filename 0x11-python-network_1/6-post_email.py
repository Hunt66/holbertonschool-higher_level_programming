#!/usr/bin/python3
""" Sends a POST request to the URL passed in with email as parameter
    dislplays body respones"""
import sys
import requests


if len(sys.argv) < 2:
    print("needs URL and email")
elif len(sys.argv) < 3:
    print("need email")
else:
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
