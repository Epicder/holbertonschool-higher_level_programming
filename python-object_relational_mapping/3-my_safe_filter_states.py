#!/usr/bin/python3
"""
avoid sql injection
"""
import sys
import MySQLdb


def get_states(username, password, database, state_name):
    """get states"""

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database, charset="utf8")
    cur = conn.cursor()
    sqlcmd = ("SELECT * FROM states " +
                "WHERE BINARY name LIKE %s ORDER BY id ASC")
    cur.execute(sqlcmd, (state_name,))
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
    state_name = sys.argv[4]
    get_states(username, password, database, state_name)