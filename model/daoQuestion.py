from sqlite3 import OperationalError
from model.abstractDao import AbstractDao
from database.db import Db
from model.question import Question
from model.daoCategory import Dao


class DaoQuestion(AbstractDao):
    def __init__(self):
        self.__database = Db
        self.__table_name = 'question'
        self.__records = []
        self.__dao_category = Dao

        fields = 'id integer NOT NULL, description varchar(255) NOT NULL, answer varchar(255) NOT NULL, category integer NOT NULL, points integer NOT NULL, date date NOT NULL, PRIMARY KEY(id AUTOINCREMENT), FOREIGN KEY(category) REFERENCES category(id)'
        self.__database.cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {self.__table_name} ({fields})')
        self.__database.connection.commit()
        # self.populate()

    def insert(self, question: Question):
        print(question.date)
        fields = 'description, answer, category, points, date'
        values = f'"{question.description}", "{question.answer}", "{question.category.id}", "{question.points}", "{question.date}"'
        try:
            self.__database.cursor.execute(
                f'INSERT INTO {self.__table_name} ({fields}) VALUES({values})')
            self.__database.connection.commit()

            question.id = self.__database.cursor.lastrowid
            self.__records.append(question)
            return True
        except OperationalError as error:
            print(error)
            self.__database.connection.rollback()
            return False

    def update(self, question: Question):
        pass

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

            category = self.__dao_category.read(record[3])

            object = Question(record[1], record[2],
                              category, record[4], record[5])
            object.id = record[0]
            self.__records.append(object)


DaoQ = DaoQuestion()
