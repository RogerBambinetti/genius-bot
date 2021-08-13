import tweepy

class Bot():
    def __init__(self):
        self.__auth = tweepy.OAuthHandler("eRUT7A5TeY1Dj4u3cTtMnMIFx", "rtVacS2yMotxcy1V2Z7YDMQbHtEXbBADWGebF2iDQPYfDLJ3KT")
        self.__auth.set_access_token("1425438439722430469-DLQ5T6LSCtf8hSnRYRSrDBGjCjsxyA", "rNFZjZonQfcqkfOsli0B6KNWLiR6YRB4EVV4brrVi30Jv")
        self.__api = tweepy.API(self.__auth)
        self.__cursor = tweepy.Cursor
    
    @property
    def api(self):
        return self.__api

    @property
    def cursor(self):
        return self.__cursor    