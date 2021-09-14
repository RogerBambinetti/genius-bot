from exception.NotExistsException import NotExistsException
from model.player import Player
from dao.daoPlayer import PlayerDao


class ControllerPlayer:

    def __init__(self):
        self.__dao = PlayerDao

    def insert(self, name, username):
        if isinstance(name, str) and isinstance(username, str):
            player = Player(name, username)
            return self.__dao.insert(player)
        else:
            raise TypeError

    def update(self, id: int, name=None, username=None):
        if isinstance(id, int):
            player = self.__dao.read(id)
            if player:
                if name:
                    if isinstance(name, str):
                        player.name = name
                    else:
                        raise TypeError
                if username:
                    if isinstance(username, str):
                        player.username = username
                    else:
                        raise TypeError

                return self.__dao.update(player)
            else:
                raise NotExistsException
        else:
            raise TypeError

    def delete(self, id: int):
        if isinstance(id, int):
            player = self.__dao.read(id)
            if player:
                return self.__dao.delete(player)
            else:
                raise NotExistsException
        else:
            raise TypeError

    def read(self, id: int):
        if isinstance(id, int):
            player = self.__dao.read(id)
            if player:
                return player
            else:
                raise NotExistsException
        else:
            raise TypeError

    def readByUsername(self, username):
        if isinstance(username, str):
            players = self.__dao.list()

            for player in players:
                if(player.username == username):
                    return player
            raise NotExistsException
        else:
            raise TypeError

    def list(self):
        return self.__dao.list()
