import json
import game
from datetime import datetime
import calendar
import time

allGames = []

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'},
        'body': json.dumps(parseText(event['body']))
    }

def parseText(submittedText):
	lines = submittedText.split('\n')
#	with lines as fp:
 #	line = fp.readline()
#		cnt = 1
#		while line:
#			line = line.split('\t')
	# 	homeTeam = line[4] == 'Highrock'
	# 	otherTeam = (line[4], line[6])[homeTeam]
	# 	subj = line[2]+(' vs ', ' at ')[homeTeam]+otherTeam
	# 	subj = subj.strip()

	# 	gameYear = datetime.now().year
	# 	gameMonthNum = list(calendar.month_abbr).index(line[1].split('-')[1])
	# 	gameDayNum = line[1].split('-')[0]
	# 	formattedGameDate = str(gameMonthNum) + '/' + str(gameDayNum) + '/' + str(gameYear)
	# 	gameTime = line[3]

	# 	allGames.append(game.game(subj, formattedGameDate, gameTime, homeTeam))
	# 	line = fp.readline()
	# 	cnt += 1
	lines[0] = lines[0] + 'added text'
	return lines

# f.write('SUBJECT, START DATE, START TIME, END DATE, END TIME, ALL DAY EVENT, DESCRIPTION, LOCATION, PRIVATE\n')

# for aGame in allGames:
# 	newRow = aGame.subject+','+ aGame.date + ',' + aGame.time + ','+ aGame.date +',' + aGame.time + ',FALSE'
# 	f.write(newRow)
# 	print(aGame.time)