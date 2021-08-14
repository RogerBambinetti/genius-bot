from model.daoPlayer import PlayerDao
from model.daoAnswer import AnswerDao
from model.player import Player
from controller.controllerAnswer import ControllerAnswer
from datetime import date


# player = Player("teste", "teste")
# PlayerDao.insert(player)

c = ControllerAnswer()
# c.insert("b", 1, 1, date(2021, 8, 14))

print(c.verifyAnswer(2, 7))
