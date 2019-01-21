#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status """
import requests


r = requests.get("https://intranet.hbtn.io/status")
print("Body response:")
print("\t- type: " + str(type(r.text)))
print("\t- content: " + str(r.content))
