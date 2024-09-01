import sqlite3


class DbManager:
    def __init__(self, db) -> None:
        print(db)
        self.con = sqlite3.connect(db)
        self.con.row_factory = sqlite3.Row

    def get_table_data(self, table, columns: tuple):
        res = self.con.execute(f'SELECT {",".join(columns)} FROM {table}')
        return res.fetchall()
