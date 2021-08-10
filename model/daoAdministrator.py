from model.abstractDao import AbstractDao
from database.db import Db
from model.administrator import Administrator

class DaoAdministrator(AbstractDao):

    def __init__(self):
        self.__database = Db
        self.__table_name = 'administrator'

        fields = 'id integer NOT NULL, name varchar(255) NOT NULL, username varchar(255) NOT NULL, email varchar(255) NOT NULL,  password varchar(255) NOT NULL, PRIMARY KEY(id AUTOINCREMENT)'        
        self.__database.cursor.execute(f'CREATE TABLE IF NOT EXISTS {self.__table_name} ({fields})')
        self.__database.connection.commit()

    @property
    def database(self):
        return self.__database

    def insert(self, administrator: Administrator):
        fields = 'name, username, email, password'
        values = f'"{administrator.name}","{administrator.username}","{administrator.email}","{administrator.password}"'
        
        self.__database.cursor.execute(f'INSERT INTO {self.__table_name} ({fields}) VALUES({values})')
        self.__database.connection.commit()

        administrator.id = self.__database.cursor.lastrowid

    def update(self, administrator: Administrator):
        fields = f'name = "{administrator.name}", username = "{administrator.username}", email = "{administrator.email}", password = "{administrator.password}"'
        
        self.__database.cursor.execute(f'UPDATE {self.__table_name} SET {fields} WHERE id = {administrator.id}')
        self.__database.connection.commit()

    def delete(self, administrator: Administrator):
        self.__database.cursor.execute(f'DELETE FROM {self.__table_name} WHERE id = {administrator.id}')
        self.__database.connection.commit()

    def read(self, administrator: Administrator):
        return self.__database.cursor.execute(f'SELECT FROM {self.__table_name} WHERE id = {administrator.id}').fetchone()
        

    def list(self):
        return self.__database.cursor.execute(f'SELECT * FROM {self.__table_name}').fetchall()
        