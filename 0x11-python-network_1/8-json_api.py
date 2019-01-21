#!/usr/bin/python3
""" takes in a letter and send request with the letter as peramiter """
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No result")
    else:
        lett = str(sys.argv[1])
        r = requests.post('http://0.0.0.0:5000/search_user', data={'q': lett})
        try:
            ans = r.json()
            if ans is not None:
                print('[' + str(ans['id']) + '] ' + str(ans['name']))
            else:
                print("No result")
        except:
            print("No result")
