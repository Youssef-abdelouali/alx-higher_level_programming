#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    dbs = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], dbs=sys.argv[3], port=3306)
    cur = dbs.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    dbs.close()
