#!/usr/bin/python3
"""Lists all states from the database starting with N hbtn_0e_0_usa"""

import MySQLdb
import sys


def main(argv):
    """func - main - args"""
    if len(argv) != 4:
        print("Enter 3 arguments")
        return

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")

    for row in cur.fetchall():
        print(row)
    db.close()

if __name__ == "__main__":
    import sys
    main(sys.argv)
