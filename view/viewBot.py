from threading import Timer
from controller.controllerBot import ControllerBot
from controller.controllerQuestion import ControllerQuestion

class ViewBot():
    def __init__(self):
        self.__controllerBot =  ControllerBot()
        self.__controllerQuestion = ControllerQuestion()
        self.__last_question = None
        self.__last_tweet = None
        
        self.initQuestionSchedule()

    def initQuestionSchedule(self):
        question = self.__controllerQuestion.readRandom()
        
        if(question.id == self.__last_question):
            return self.initQuestionSchedule()

        if(question):
            tweet = self.__controllerBot.makeTweet(question.description)
            
            if(tweet):
                self.__last_question = question.id
                self.__last_tweet = tweet.id_str
                print('perguntou')

        Timer(20.0, self.verifyAnswers, ()).start()
    
    def verifyAnswers(self):
        replies = self.__controllerBot.getTweetReplies(self.__last_tweet)
        
        for reply in replies:
            self.__controllerQuestion.verifyAnswer(self.__last_question, reply.text)
            print(reply.text)
            print(reply.author.screen_name)
        
        self.initQuestionSchedule()