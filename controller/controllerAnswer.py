from controller.controllerQuestion import ControllerQuestion
from controller.controllerPlayer import ControllerPlayer
from model.answer import Answer
from model.daoAnswer import AnswerDao
from datetime import date


class ControllerAnswer:
    def __init__(self):
        self.__dao = AnswerDao
        self.__controller_question = ControllerQuestion()
        self.__controller_player = ControllerPlayer()

    def insert(self, alternative: str, id_player: int, id_question: int, date: date):
        if isinstance(alternative, str) and isinstance(id_player, int) and isinstance(id_question, int):
            player = self.__controller_player.read(id_player)
            question = self.__controller_question.read(id_question)
            if player and question:
                list = self.__dao.list()
                for answer in list:
                    if answer.question != question or answer.player != player:
                        alternative = alternative.replace(
                            '@thegeniusbot', '').strip().upper()
                        answer = Answer(alternative, player, question, date)
                        return self.__dao.insert(answer)
                    else:
                        return False
        else:
            raise TypeError

    def update(self, id: int, alternative=None, id_player=None, id_question=None, date=None):
        if isinstance(id, int):
            answer = self.__dao.read(id)

            if alternative:
                if isinstance(alternative, str):
                    alternative = alternative.replace(
                        '@thegeniusbot', '').strip().upper()
                    answer.alternative = alternative
                else:
                    raise TypeError
            if id_player:
                if isinstance(id_player, int):
                    player = self.__controller_player.read(id_player)
                    if player:
                        answer.player = player
                else:
                    raise TypeError
            if id_question:
                if isinstance(id_question, int):
                    question = self.__controller_question.read(id_question)
                    if question:
                        answer.question = question
                else:
                    raise TypeError
            if date:
                answer.date = date

            return self.__dao.update(answer)
        else:
            raise TypeError

    def delete(self, id: int):
        if isinstance(id, int):
            answer = self.__dao.read(id)
            return self.__dao.delete(answer)
        else:
            raise TypeError

    def read(self, id: int):
        if isinstance(id, int):
            return self.__dao.read(id)
        else:
            raise TypeError

    def list(self):
        return self.__dao.list()

    def verifyAnswer(self, id_player: int, id_question: int):
        if isinstance(id_player, int) and isinstance(id_question, int):
            player = self.__controller_player.read(id_player)
            question = self.__controller_question.read(id_question)
            list = self.__dao.list()
            for answer in list:
                if answer.question == question and answer.player == player:
                    return answer.verifyAnswer()
        else:
            raise TypeError
