from sqlite3 import OperationalError
from model.abstractDao import AbstractDao
from database.db import Db
from model.player import Player

class DaoPlayer(AbstractDao):

    def __init__(self):
        self.__database = Db
        self.__table_name = 'player'
        self.__records = []

        fields = 'id integer NOT NULL, name varchar(255) NOT NULL, username varchar(255) NOT NULL, PRIMARY KEY(id AUTOINCREMENT)'        
        self.__database.cursor.execute(f'CREATE TABLE IF NOT EXISTS {self.__table_name} ({fields})')
        self.__database.connection.commit()
        self.populate()

    @property
    def database(self):
        return self.__database

    def insert(self, player: Player):
        fields = 'name, username'
        values = f'"{player.name}","{player.username}"'
        
        try:
            self.__database.cursor.execute(f'INSERT INTO {self.__table_name} ({fields}) VALUES({values})')
            self.__database.connection.commit()

            player.id = self.__database.cursor.lastrowid
            self.__records.append(player)
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def update(self, player: Player):
        fields = f'name = "{player.name}", username = "{player.username}"'
        
        try:
            self.__database.cursor.execute(f'UPDATE {self.__table_name} SET {fields} WHERE id = {player.id}')
            self.__database.connection.commit()
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def delete(self, player: Player):
        try:
            self.__database.cursor.execute(f'DELETE FROM {self.__table_name} WHERE id = {player.id}')
            self.__database.connection.commit()
            
            self.__records.remove(player)
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False        

    def read(self, id: int):
        for record in self.__records:
            if(record.id == id):
                return record
        

    def list(self):
        return self.__records
        
    def populate(self):
        records = self.__database.cursor.execute(f'SELECT * FROM {self.__table_name}').fetchall()

        for record in records:
            object = Player(record[1],record[2])
            object.id = record[0]
            self.__records.append(object)

Dao = DaoPlayer()