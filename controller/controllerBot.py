from model.bot import Bot
from tweepy import TweepError

class ControllerBot():
    def __init__(self):
        self.__bot = Bot()
    
    def makeTweet(self, text):
        try:
            return self.__bot.api.update_status(text)
        except TweepError as error:
            return False

    def likeTweet(self, id):
        try:
            self.__bot.api.create_favorite(id)
            return True
        except TweepError as error:
            return False

    def deleteTweet(self, id):
        try:
            self.__bot.api.destroy_status(id)
            return True
        except TweepError as error:
            return False

    def getTweetReplies(self, id):
        user_name = "@thegeniusbot"

        replies=[]
        for tweet in self.__bot.cursor(self.__bot.api.search,q='to:'+user_name, result_type='recent', timeout=999999).items(1000):
            if hasattr(tweet, 'in_reply_to_status_id_str'):
                if (tweet.in_reply_to_status_id_str==id):
                    replies.append(tweet)
        
        return replies