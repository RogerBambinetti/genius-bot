import time
from datetime import date
from controller.controllerBot import ControllerBot
from controller.controllerAnswer import ControllerAnswer
from controller.controllerPlayer import ControllerPlayer
from controller.controllerQuestion import ControllerQuestion
from controller.controllerRanking import ControllerRanking

class ViewBot():
    def __init__(self):
        self.__controllerBot =  ControllerBot()
        self.__controllerQuestion = ControllerQuestion()
        self.__controllerAnswer =  ControllerAnswer()
        self.__controllerPlayer =  ControllerPlayer()
        self.__controllerRanking =  ControllerRanking()
        self.__last_question = None
        self.__last_tweet = None
        
        self.initQuestionSchedule()
        self.initDailyRankingSchedule()

    def initDailyRankingSchedule(self):
        time.sleep(60 * 60 * 24)
        ranking = self.__controllerRanking.getDailyRanking()
        
        if self.__controllerBot.makeTweet(ranking):
            print('Ranking diário publicado')
    
        self.initDailyRankingSchedule()

    def initQuestionSchedule(self):
        question = self.__controllerQuestion.readRandom()
        
        if(question.id == self.__last_question):
            return self.initQuestionSchedule()

        if(question):
            tweet = self.__controllerBot.makeTweet(question.description)
            
            if(tweet):
                self.__last_question = question.id
                self.__last_tweet = tweet.id_str
                print('Pergunta publicada')

        self.verifyAnswers()
    
    def verifyAnswers(self):
        time.sleep(60 * 30)

        replies = self.__controllerBot.getTweetReplies(self.__last_tweet)
        
        for reply in replies:
            player = self.__controllerPlayer.readByUsername(reply.author.screen_name)
            if (not player):
                self.__controllerPlayer.insert(reply.author.name, reply.author.screen_name)
                player = self.__controllerPlayer.readByUsername(reply.author.screen_name)
            
            if self.__controllerAnswer.insert(reply.text,player.id, self.__last_question, date.today().strftime("%d/%m/%Y")):

                if self.__controllerAnswer.verifyAnswer(player.id, self.__last_question):
                    self.__controllerBot.likeTweet(reply.id_str)

        print('Respostas verificadas')
        self.initQuestionSchedule()