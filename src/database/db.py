from sqlite3 import connect
from typing import List


class Database:
    def __init__(self, db: str) -> None:
        self.__connection = connect(db, check_same_thread=False)
        self.__cursor = self.__connection.cursor()

    def create(self, name: str) -> None:
        with self.__connection:
            self.__cursor.execute(
                'INSERT OR IGNORE INTO acoes (nome) VALUES (?)',
                (name,)
            )
            self.__connection.commit()

    def read(self) -> List:
        with self.__connection:
            self.__cursor.execute('SELECT * FROM acoes')

            return self.__cursor.fetchall()

    def delete(self, name: str) -> None:
        with self.__connection:
            self.__cursor.execute(
                'DELETE FROM acoes WHERE nome=?',
                (name,)
            )
            self.__connection.commit()
