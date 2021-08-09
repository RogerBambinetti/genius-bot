from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

class Database():
    def __init__(self):
        self.__engine = create_engine('sqlite:///database/database.db', echo=True)
        self.__session = sessionmaker(bind=self.__engine)()
        self.__base = declarative_base(bind=self.__engine)

    @property
    def engine(self):
        return self.__engine

    @property
    def session(self):
        return self.__session

    @property
    def base(self):
        return self.__base

Db = Database()