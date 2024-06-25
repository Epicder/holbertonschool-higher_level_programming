#!/usr/bin/python3
"""
Write a script that list cities
"""
import sys
import MySQLdb


def get_states(username, password, database, state_name):
    """get cities"""

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database, charset="utf8")
    cur = conn.cursor()
    sqlquery = ("SELECT cities.name FROM cities " +
                "JOIN states ON cities.state_id = states.id " +
                "WHERE states.name LIKE %s ORDER BY cities.id ASC")
    
    cur.execute(sqlquery, (state_name,))
    query_rows = cur.fetchall()
    print(", ".join(a[0] for a in query_rows))
    cur.close()
    conn.close()


if __name__ == '__main__':
    """comment"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    get_states(username, password, database, state_name)
