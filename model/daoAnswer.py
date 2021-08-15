from sqlite3 import OperationalError
from model.abstractDao import AbstractDao
from database.db import Db
from model.answer import Answer
from model.daoQuestion import QuestionDao
from model.daoPlayer import PlayerDao


class DaoAnswer(AbstractDao):
    def __init__(self):
        self.__database = Db
        self.__table_name = 'answer'
        self.__records = []
        self.__dao_question = QuestionDao
        self.__dao_player = PlayerDao
        try:
            fields = 'id integer NOT NULL, alternative varchar(255) NOT NULL, player integer NOT NULL, question integer NOT NULL, date date NOT NULL, PRIMARY KEY(id AUTOINCREMENT), FOREIGN KEY(player) REFERENCES player(id), FOREIGN KEY(question) REFERENCES question(id)'
            self.__database.cursor.execute(
                f'CREATE TABLE IF NOT EXISTS {self.__table_name} ({fields})')
            self.__database.connection.commit()
            self.populate()
        except OperationalError as error:
            self.__database.connection.rollback()

    def insert(self, answer: Answer):
        fields = 'alternative, player, question, date'
        values = f'"{answer.alternative}", "{answer.player.id}", "{answer.question.id}", "{answer.date}"'
        try:
            self.__database.cursor.execute(
                f'INSERT INTO {self.__table_name} ({fields}) VALUES({values})')
            self.__database.connection.commit()

            answer.id = self.__database.cursor.lastrowid
            self.__records.append(answer)
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def update(self, answer: Answer):
        fields = f'alternative = "{answer.alternative}", player = "{answer.player.id}", question = "{answer.question.id}", date = "{answer.date}"'

        try:
            self.__database.cursor.execute(
                f'UPDATE {self.__table_name} SET {fields} WHERE id = {answer.id}')
            self.__database.connection.commit()
            return True
        except OperationalError as error:
            self.__database.connection.rollback()
            return False

    def delete(self, answer: Answer):
        try:
            self.__database.cursor.execute(
                f'DELETE FROM {self.__table_name} WHERE id = {answer.id}')
            self.__database.connection.commit()

            for record in self.__records:
                if(record.id == answer.id):
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

            player = self.__dao_player.read(record[2])
            question = self.__dao_question.read(record[3])

            object = Answer(record[1], player,
                            question, record[4])
            object.id = record[0]
            self.__records.append(object)


AnswerDao = DaoAnswer()
