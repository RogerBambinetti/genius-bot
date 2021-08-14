from datetime import date
from controller.controllerAnswer import ControllerAnswer
from controller.controllerPlayer import ControllerPlayer
from controller.controllerQuestion import ControllerQuestion

class ControllerRanking():
    def __init__(self):
        self.__controllerAnswer = ControllerAnswer()

    def getDailyRanking(self):
        answers = self.__controllerAnswer.list()
        dailyAnswers = []
        for answer in answers:

            today = date.today().strftime("%d/%m/%Y")
            if(answer.date == today):
                dailyAnswers.append(answer)
        
        rightAnswers = []
        for dailyAnswer in dailyAnswers:
            if(self.__controllerAnswer.verifyAnswer(dailyAnswer.player.id, dailyAnswer.question.id)):
                rightAnswers.append(dailyAnswer)

        players = []
        for rightAnswer in rightAnswers:
            if rightAnswer.player not in players:
                players.append(rightAnswer.player)
        
        scores = []
        for player in players:
            score = 0
            for rightAnswer in rightAnswers:
                if rightAnswer.player == player:
                    score = score + rightAnswer.question.points
            scores.append(score)
        
        for i in range(len(players)):
            for j in range(len(players) - 1):
                if scores[j] < scores[j +1]:
                    oldScore = scores[j]
                    oldPlayer = players[j]

                    scores[j] = scores[j+1]
                    scores[j+1] = oldScore

                    players[j] = players[j+1]
                    players[j+1] = oldPlayer
        
        ranking = f'🏆 Ranking Diário - {today} 🏆\n'
        for i in range(10):
            if(i < len(players)):
                ranking += f'@{players[i].username}: {scores[i]} pontos \n'

        return ranking
            
    def getGeneralRanking(self):
        answers = self.__controllerAnswer.list()
        
        rightAnswers = []
        for answer in answers:
            if(self.__controllerAnswer.verifyAnswer(answer.player.id, answer.question.id)):
                rightAnswers.append(answer)

        players = []
        for rightAnswer in rightAnswers:
            if rightAnswer.player not in players:
                players.append(rightAnswer.player)
        
        scores = []
        for player in players:
            score = 0
            for rightAnswer in rightAnswers:
                if rightAnswer.player == player:
                    score = score + rightAnswer.question.points
            scores.append(score)
        
        for i in range(len(players)):
            for j in range(len(players) - 1):
                if scores[j] < scores[j +1]:
                    oldScore = scores[j]
                    oldPlayer = players[j]

                    scores[j] = scores[j+1]
                    scores[j+1] = oldScore

                    players[j] = players[j+1]
                    players[j+1] = oldPlayer
        
        ranking = f'🏆 Ranking Geral 🏆\n'
        for i in range(10):
            if(i < len(players)):
                ranking += f'@{players[i].username}: {scores[i]} pontos \n'

        return ranking
  
