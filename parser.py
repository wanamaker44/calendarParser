import game

filepath = "C:/Users/bill/Workspace/scheduleInput.txt"

newGame = game.game('subjectasfdkjdsalfkj', 'date', 'time')
allGames = []

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       line = line.split('\t')
       print(line)
       homeTeam = line[4] == 'Highrock'
       otherTeam = (line[4], line[6])[homeTeam]
       subj = line[2], (' vs ', ' at ')[homeTeam], otherTeam
       allGames.append(game.game(subj, line[1], line[3]))
       line = fp.readline()
       cnt += 1

for aGame in allGames:
	print(aGame.subject, ',', aGame.date, ',', aGame.time, ',', aGame.date, ',', aGame.time, 'FALSE')