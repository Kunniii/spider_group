import sqlite3
from os.path import abspath
import pandas as pd


class Database:
    def __init__(self, file) -> None:
        self.connection = sqlite3.connect(abspath(file))
        self.cursor = self.connection.cursor()
        self.init_db()

    def __del__(self) -> None:
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def init_db(self):
        sql = """CREATE TABLE IF NOT EXISTS Student (
                    RollNumber TEXT PRIMARY KEY,
                    Surname TEXT,
                    Middle_name TEXT,
                    Given_name TEXT
                )"""
        self.cursor.execute(sql)
        self.connection.commit()

    def add_data(self, data: tuple) -> bool:
        try:
            self.cursor.execute(
                "INSERT INTO Student (RollNumber, Surname, Middle_name, Given_name) VALUES (?, ?, ?, ?)",
                data,
            )
            self.connection.commit()
            return True
        except:
            return False

    def add_data_many(self, data: list[tuple]) -> bool:
        try:
            self.cursor.executemany(
                "INSERT INTO Student (RollNumber, Surname, Middle_name, Given_name) VALUES (?, ?, ?, ?)",
                data,
            )
            self.connection.commit()
            return True
        except:
            return False

    def to_excel(self, file):
        self.cursor.execute('SELECT * FROM Student')
        rows = self.cursor.fetchall()
        column_names = [description[0]
                        for description in self.cursor.description]
        df = pd.DataFrame(rows, columns=column_names)
        df.to_excel(abspath(file), index=False)
