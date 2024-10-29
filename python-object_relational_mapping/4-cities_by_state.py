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
    query = """SELECT cities.id, cities.name, states.name
                FROM cities LEFT JOIN states
                ON cities.state_id = states.id"""
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()

    for row in rows:
        print(row)

    c.close()
    db.close()
