from controller.controllerQuestion import ControllerQuestion
from controller.controllerPlayer import ControllerPlayer
from model.answer import Answer
from model.daoAnswer import AnswerDao


class ControllerAnswer:
    def __init__(self):
        self.__dao = AnswerDao
        self.__controller_question = ControllerQuestion()
        self.__controller_player = ControllerPlayer()

    def insert(self, alternative, id_player, id_question, date):
        player = self.__controller_player.read(id_player)
        question = self.__controller_question.read(id_question)
        if player and question:
            list = self.__dao.list
            for answer in list:
                if answer.question != question or answer.player != player:
                    alternative = alternative.replace(
                        '@thegeniusbot', '').strip().upper()
                    answer = Answer(alternative, player, question, date)
                    return self.__dao.insert(answer)
                else:
                    return False

    def update(self, id: int, alternative=None, id_player=None, id_question=None, date=None):
        answer = self.__dao.read(id)

        if alternative:
            alternative = alternative.replace(
                '@thegeniusbot', '').strip().upper()
            answer.alternative = alternative
        if id_player:
            player = self.__controller_player.read(id_player)
            if player:
                answer.player = player
        if id_question:
            question = self.__controller_question.read(id_question)
            if question:
                answer.question = question
        if date:
            answer.date = date

        return self.__dao.update(answer)

    def delete(self, id: int):
        answer = self.__dao.read(id)
        return self.__dao.delete(answer)

    def read(self, id: int):
        return self.__dao.read(id)

    def list(self):
        return self.__dao.list()

    def verifyAnswer(self, id_player, id_question):
        player = self.__controller_player.read(id_player)
        question = self.__controller_question.read(id_question)
        list = self.__dao.list
        for answer in list:
            if answer.question == question and answer.player == player:
                return answer.verifyAnswer()
            else:
                return False
