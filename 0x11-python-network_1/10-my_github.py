#!/usr/bin/python3
""" takes github credentials and uses github api to display id """
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("requires username and password")
    elif len(sys.argv) < 3:
        print("requires password")
    else:
        r = requests.get("https://api.github.com/user",
                         auth=(sys.argv[1], sys.argv[2]))
        ans = r.json()
        print(ans.get('id'))
