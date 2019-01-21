#!/usr/bin/python3
""" takes a string nd sends a search request to star wars api"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("needs arg")
    else:
        r = requests.post('https://swapi.co/api/people',
                          params={'search': sys.argv[1]})
        ans = r.json()
        print("Number of results: " + str(ans['count']))
        for itm in ans['results']:
            print(itm['name'])
