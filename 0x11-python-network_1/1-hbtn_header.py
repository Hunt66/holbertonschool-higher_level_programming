#!/usr/bin/python3
""" takes a URL sends request and displays the value of X-Request-Id found in
     the header """

import urllib.request
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("URL required")
    else:
        with urllib.request.urlopen(sys.argv[1]) as r:
            stf = r.getheaders()
            for ans in stf:
                if 'X-Request-Id' in ans:
                    print(ans[1])
