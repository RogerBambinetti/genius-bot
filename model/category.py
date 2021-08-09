from sqlalchemy import Column, Integer, String
from database.db import Db

Base = Db.base


class Category(Base):

    __tablename__ = 'Category'

    id = Column(Integer, primary_key=True)
    _name = Column('name', String)

    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

Base.metadata.create_all()