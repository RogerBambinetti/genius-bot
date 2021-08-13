from sqlite3 import OperationalError
from model.abstractDao import AbstractDao
from database.db import Db
from model.question import Question


class DaoQuestion(AbstractDao):
    def __init__(self):
        self.__database = Db
        self.__table_name = 'question'
        self.__records = []

        fields = 'id integer NOT NULL, name varchar(255) NOT NULL, PRIMARY KEY(id AUTOINCREMENT)'
        self.__database.cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {self.__table_name} ({fields})')
        self.__database.connection.commit()
        self.populate()

    def insert(self, question: Question):
        fields = 'name'
        values = f'"{question.name}"'
        try:
            self.__database.cursor.execute(
                f'INSERT INTO {self.__table_name} ({fields}) VALUES({values})')
            self.__database.connection.commit()

            question.id = self.__database.cursor.lastrowid
            self.__records.append(question)
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def update(self, question: Question):
        fields = f'name = "{question.name}"'
        try:
            self.__database.cursor.execute(
                f'UPDATE {self.__table_name} SET {fields} WHERE id = {question.id}')
            self.__database.connection.commit()
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def delete(self, question: Question):
        try:
            self.__database.cursor.execute(
                f'DELETE FROM {self.__table_name} WHERE id = {question.id}')
            self.__database.connection.commit()

            for record in self.__records:
                if(record.id == question.id):
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

            object = Question(record[1], record[2],
                              record[3], record[4], record[5])
            object.id = record[0]
            self.__records.append(object)


Dao = DaoQuestion()
