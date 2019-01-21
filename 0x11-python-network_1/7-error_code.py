#!/usr/bin/python3
""" takes URL and sends a request to display the body response """
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("needs URL and email")
    else:
        r = requests.get(sys.argv[1])
        try:
            r.raise_for_status()
            print(r.content.decode('utf-8'))
        except:
            print("Error code: " + str(r.status_code))
