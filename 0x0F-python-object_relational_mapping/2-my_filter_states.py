#!/usr/bin/python3
""" lists all instences of sacific state """

import MySQLdb
import sys


def main(argv):
    """func - main - args"""
    if len(argv) != 5:
        print("Enter 4 arguments")
        return

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = BINARY '{}'".format(argv[4]))

    for row in cur.fetchall():
        print(row)
    db.close()

if __name__ == "__main__":
    import sys
    main(sys.argv)
