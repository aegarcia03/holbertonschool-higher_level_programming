#!/usr/bin/python3
""" Nameless module for running SQL """


if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )
    query = """SELECT * FROM states WHERE name LIKE BINARY "N%" ORDER BY id ASC"""
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()

    for row in rows:
        print(row)

    c.close()
    db.close()
