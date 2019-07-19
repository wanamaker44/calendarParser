import game
import datetime

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

fileName = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '.csv'

f = open(fileName, "a")

f.write('SUBJECT, START DATE, START TIME, END DATE, END TIME, ALL DAY EVENT, DESCRIPTION, LOCATION, PRIVATE\n')

for aGame in allGames:
	newRow = aGame.subject+','+aGame.date+','+aGame.time+','+aGame.date+','+aGame.time+',FALSE'
	f.write(newRow)

f.close()