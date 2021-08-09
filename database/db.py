from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Database():
    def __init__(self):
        self.__engine = create_engine('sqlite:///database.db', echo=True)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    @property
    def engine(self):
        return self.__engine

    @property
    def session(self):
        return self.__session