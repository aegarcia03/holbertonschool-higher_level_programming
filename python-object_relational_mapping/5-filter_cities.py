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
        database=sys.argv[3],
    )
    query = """SELECT name FROM cities WHERE BINARY state_id =
                (SELECT id FROM states WHERE name = %s)"""
    c = db.cursor()
    c.execute(query, ((sys.argv[4]), ))
    rows = c.fetchall()

    result = [row[0] for row in rows]
    print(", ".join(result))

    c.close()
    db.close()
