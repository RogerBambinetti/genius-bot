import time
from model.bot import Bot
from datetime import date
from controller.controllerAnswer import ControllerAnswer
from controller.controllerPlayer import ControllerPlayer
from controller.controllerQuestion import ControllerQuestion
from controller.controllerRanking import ControllerRanking
from tweepy import TweepError
from exception.InsufficientDataException import InsufficientDataException

class ControllerBot():
    def __init__(self):
        self.__bot = Bot()

        self.__controllerQuestion = ControllerQuestion()
        self.__controllerAnswer =  ControllerAnswer()
        self.__controllerPlayer =  ControllerPlayer()
        self.__controllerRanking =  ControllerRanking()

        self.__last_question = None
        self.__last_tweet = None
        
        self.initQuestionSchedule()
        self.initDailyRankingSchedule()

    def makeTweet(self, text: str):
        if isinstance(text, str):
            try:
                return self.__bot.api.update_status(text)
            except TweepError as error:
                return False
        else:
            raise TypeError

    def likeTweet(self, id: str):
        if isinstance(id, str):
            try:
                self.__bot.api.create_favorite(id)
                return True
            except TweepError as error:
                return False
        else:
            raise TypeError

    def deleteTweet(self, id: str):
        if isinstance(id, str):
            try:
                self.__bot.api.destroy_status(id)
                return True
            except TweepError as error:
                return False
        else:
            raise TypeError

    def getTweetReplies(self, id: str):
        if isinstance(id, str):
            user_name = "@thegeniusbot"

            replies = []
            for tweet in self.__bot.cursor(self.__bot.api.search, q='to:'+user_name, result_type='recent', timeout=999999).items(1000):
                if hasattr(tweet, 'in_reply_to_status_id_str'):
                    if (tweet.in_reply_to_status_id_str == id):
                        replies.append(tweet)

            return replies
        else:
            raise TypeError

    def initDailyRankingSchedule(self):
        time.sleep(60 * 60 * 24)
        try:
            ranking = self.__controllerRanking.getDailyRanking()
            
            if self.makeTweet(ranking):
                print('Ranking diário publicado')
        except InsufficientDataException:
            pass
    
        self.initDailyRankingSchedule()

    def initQuestionSchedule(self):
        question = self.__controllerQuestion.readRandom()
        
        if(question.id == self.__last_question):
            return self.initQuestionSchedule()

        if(question):
            tweet = self.makeTweet(question.description)
            
            if(tweet):
                self.__last_question = question.id
                self.__last_tweet = tweet.id_str
                print('Pergunta publicada')

        self.verifyAnswers()
    
    def verifyAnswers(self):
        time.sleep(60 * 30)

        replies = self.getTweetReplies(self.__last_tweet)
        
        for reply in replies:
            player = self.__controllerPlayer.readByUsername(reply.author.screen_name)
            if (not player):
                self.__controllerPlayer.insert(reply.author.name, reply.author.screen_name)
                player = self.__controllerPlayer.readByUsername(reply.author.screen_name)
            
            if self.__controllerAnswer.insert(reply.text,player.id, self.__last_question, date.today().strftime("%d/%m/%Y")):

                if self.__controllerAnswer.verifyAnswer(player.id, self.__last_question):
                    self.likeTweet(reply.id_str)

        print('Respostas verificadas')
        self.initQuestionSchedule()