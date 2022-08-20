import sqlite3


def connection_date_base(sql):
    with sqlite3.connect("netflix.db") as connection:
        connection.row_factory = sqlite3.Row
        result = connection.execute(sql).fetchall()
        return result
