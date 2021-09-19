from exception.NotExistsException import NotExistsException
from model.player import Player
from dao.daoPlayer import PlayerDao


class ControllerPlayer:

    def __init__(self):
        self.__dao = PlayerDao

    def insert(self, name, username):
        try:
            if isinstance(name, str) and isinstance(username, str):
                player = Player(name, username)
                return self.__dao.insert(player)
            else:
                raise TypeError
        except Exception:
            pass

    def update(self, id: int, name: str, username: str):
        try:
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
                raise TypeError
        except Exception:
            pass

    def delete(self, id: int):
        try:
            if isinstance(id, int):
                player = self.__dao.read(id)
                if player:
                    return self.__dao.delete(player)
            else:
                raise TypeError
        except Exception:
            pass

    def read(self, id: int):
        try:
            if isinstance(id, int):
                player = self.__dao.read(id)
                if player:
                    return player
                else:
                    return False
            else:
                raise TypeError
        except Exception:
            pass

    def readByUsername(self, username):
        try:
            if isinstance(username, str):
                players = self.__dao.list()

                for player in players:
                    if(player.username == username):
                        return player
            else:
                raise TypeError
        except Exception:
            pass

    def list(self):
        return self.__dao.list()
