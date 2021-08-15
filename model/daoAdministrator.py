from sqlite3 import OperationalError
from model.abstractDao import AbstractDao
from database.db import Db
from model.administrator import Administrator


class DaoAdministrator(AbstractDao):

    def __init__(self):
        self.__database = Db
        self.__table_name = 'administrator'
        self.__records = []
        try:
            fields = 'id integer NOT NULL, name varchar(255) NOT NULL, username varchar(255) NOT NULL, email varchar(255) NOT NULL,  password varchar(255) NOT NULL, PRIMARY KEY(id AUTOINCREMENT)'
            self.__database.cursor.execute(
                f'CREATE TABLE IF NOT EXISTS {self.__table_name} ({fields})')
            self.__database.connection.commit()
            self.populate()
        except OperationalError as error:
            self.__database.connection.rollback()

    def insert(self, administrator: Administrator):
        fields = 'name, username, email, password'
        values = f'"{administrator.name}","{administrator.username}","{administrator.email}","{administrator.password}"'

        try:
            self.__database.cursor.execute(
                f'INSERT INTO {self.__table_name} ({fields}) VALUES({values})')
            self.__database.connection.commit()

            administrator.id = self.__database.cursor.lastrowid
            self.__records.append(administrator)
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def update(self, administrator: Administrator):
        fields = f'name = "{administrator.name}", username = "{administrator.username}", email = "{administrator.email}", password = "{administrator.password}"'

        try:
            self.__database.cursor.execute(
                f'UPDATE {self.__table_name} SET {fields} WHERE id = {administrator.id}')
            self.__database.connection.commit()
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def delete(self, administrator: Administrator):
        try:
            self.__database.cursor.execute(
                f'DELETE FROM {self.__table_name} WHERE id = {administrator.id}')
            self.__database.connection.commit()

            for record in self.__records:
                if(record.id == administrator.id):
                    self.__records.remove(record)
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

        records = self.__database.cursor.execute(
            f'SELECT * FROM {self.__table_name}').fetchall()

        for record in records:
            object = Administrator(
                record[1], record[2], record[3], record[4])
            object.id = record[0]
            self.__records.append(object)


AdministratorDao = DaoAdministrator()
