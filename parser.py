import game
import datetime
import calendar

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
       allGames.append(game.game(subj, line[1], line[3]))
       line = fp.readline()
       cnt += 1

fileName = 'output/' + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '.csv'

f = open(fileName, "a")

f.write('SUBJECT, START DATE, START TIME, END DATE, END TIME, ALL DAY EVENT, DESCRIPTION, LOCATION, PRIVATE\n')

gameYear = datetime.datetime.now().year

for aGame in allGames:
	gameMonthNum = list(calendar.month_abbr).index(aGame.date.split('-')[1])
	gameDayNum = aGame.date.split('-')[0]
	newRow = aGame.subject+','+ str(gameMonthNum) + '/' + str(gameDayNum) + '/' + str(gameYear) + ','+aGame.time+','+aGame.date+','+aGame.time+',FALSE'
	f.write(newRow)

f.close()