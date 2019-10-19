import game
from datetime import datetime
import calendar
import time

filepath = "C:/Users/bill/Workspace/scheduleInput.txt"
allGames = []

with open(filepath) as fp:
	line = fp.readline()
	cnt = 1
	while line:
		line = line.split('\t')
		homeTeam = line[4] == 'Highrock'
		otherTeam = (line[4], line[6])[homeTeam]
		subj = line[2]+(' vs ', ' at ')[homeTeam]+otherTeam
		subj = subj.strip()

		gameYear = datetime.now().year
		gameMonthNum = list(calendar.month_abbr).index(line[1].split('-')[1])
		gameDayNum = line[1].split('-')[0]
		formattedGameDate = str(gameMonthNum) + '/' + str(gameDayNum) + '/' + str(gameYear)
		gameTime = line[3]

		allGames.append(game.game(subj, formattedGameDate, gameTime, homeTeam))
		line = fp.readline()
		cnt += 1

fileName = 'output/' + datetime.now().strftime("%Y%m%d%H%M%S") + '.csv'

#f = open(fileName, "a")

#f.write('SUBJECT, START DATE, START TIME, END DATE, END TIME, ALL DAY EVENT, DESCRIPTION, LOCATION, PRIVATE\n')

for aGame in allGames:

	newRow = aGame.subject+','+ aGame.date + ',' + aGame.time + ','+ aGame.date +',' + aGame.time + ',FALSE'
#	f.write(newRow)
	print(aGame.time)

#f.close()

def getHello():
	return 'payload was received. good work idiot'