from model.question import Question
from model.player import Player
from datetime import date


class Answer():
    def __init__(self, alternative: str, player: Player, question: Question, date: date):
        self.__id = None
        self.__alternative = alternative
        if isinstance(player, Player):
            self.__player = player
        else:
            raise TypeError
        if isinstance(question, Question):
            self.__question = question
        else:
            raise TypeError
        self.__date = date

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def alternative(self):
        return self.__alternative

    @alternative.setter
    def alternative(self, alternative: str):
        self.__alternative = alternative

    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, player: Player):
        if isinstance(player, Player):
            self.__player = player

    @property
    def question(self):
        return self.__question

    @question.setter
    def question(self, question: Question):
        if isinstance(question, Question):
            self.__question = question

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    def verifyAnswer(self):
        if self.__question.answer == self.__alternative:
            return True
        else:
            return False
