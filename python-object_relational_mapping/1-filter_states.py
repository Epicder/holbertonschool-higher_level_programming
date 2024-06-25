#!/usr/bin/python3
"""
Write a script that list all states that start with N
"""
import sys
import MySQLdb


def get_states(username, password, database):
    """get states starting with N"""

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states " +
                "WHERE BINARY name LIKE 'N%' ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == '__main__':
    """comment"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    get_states(username, password, database)
