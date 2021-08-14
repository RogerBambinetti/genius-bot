from sqlite3 import OperationalError
from model.abstractDao import AbstractDao
from database.db import Db
from model.category import Category


class DaoCategory(AbstractDao):
    def __init__(self):
        self.__database = Db
        self.__table_name = 'category'
        self.__records = []

        fields = 'id integer NOT NULL, name varchar(255) NOT NULL, PRIMARY KEY(id AUTOINCREMENT)'
        self.__database.cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {self.__table_name} ({fields})')
        self.__database.connection.commit()
        self.populate()

    def insert(self, category: Category):
        fields = 'name'
        values = f'"{category.name}"'
        try:
            self.__database.cursor.execute(
                f'INSERT INTO {self.__table_name} ({fields}) VALUES({values})')
            self.__database.connection.commit()

            category.id = self.__database.cursor.lastrowid
            self.__records.append(category)
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def update(self, category: Category):
        fields = f'name = "{category.name}"'
        try:
            self.__database.cursor.execute(
                f'UPDATE {self.__table_name} SET {fields} WHERE id = {category.id}')
            self.__database.connection.commit()
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def delete(self, category: Category):
        try:
            self.__database.cursor.execute(
                f'DELETE FROM {self.__table_name} WHERE id = {category.id}')
            self.__database.connection.commit()

            for record in self.__records:
                if(record.id == category.id):
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
            object = Category(record[1])
            object.id = record[0]
            self.__records.append(object)


CategoryDao = DaoCategory()
