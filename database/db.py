import sqlite3

class Database():
    def __init__(self):
        self.__connection = sqlite3.connect('./database/database.db')

    @property
    def connection(self):
        return self.__connection