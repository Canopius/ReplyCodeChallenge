def processInput(toProcess, enemyInfo, caseNo):
	# Line by line
	output = 0
	playerLoc = 0
	dead = 0

	meta = list(map(int,toProcess.strip().split(" ")))
	
	maxY = meta[1]
	maxEnemies = meta[2]
	shotsPerRound = meta[3]
	damagePerShot = meta[4]
	damageReduction = meta[5]

	enemies = [[] for _ in range(maxY)]
	for i in range(len(enemyInfo)):
		enemies[enemyInfo[i][3]].append(enemyInfo[i][1])


	while dead < maxEnemies:
		shots = shotsPerRound
		output += 1
		playerLoc += 1

		if playerLoc >= maxY:
			playerLoc = 0
		
		for y in (list(range(playerLoc, maxY)) + list(range(0, playerLoc))):
			damage = damagePerShot - (damageReduction * y)
			toRemove = []

			for j in range(len(enemies[y])):
				if shots <= 0:
					break
				
				shots -= 1
				enemies[y][j] -= damage

				if enemies[y][j] <= 0:
					toRemove.append(enemies[y][j])
					dead += 1

			for i in range(len(toRemove)):
				enemies[y].remove(toRemove[i])



	setOutput(output, caseNo)

def setOutput(output, caseNo):
	f = open("output.txt", "a")
	f.write(f"Case #{caseNo}: {output}\n")
	f.close()

def getInput():
	caseNo = 1
	# Clears out the output file
	f = open("output.txt", "w")
	f.write("")
	f.close()

	with open("input.txt") as f:
		f.readline() # Stops the first line being sent off for processing
		for line in f:
			enemyNo = list(map(int,line.strip().split(" ")))[2]
			enemyInfo = []
			for i in range(enemyNo):
				enemyInfo.append(list(map(int,f.readline().strip().split(" "))))
			processInput(line, enemyInfo, caseNo)
			caseNo += 1

if __name__ == "__main__":
	getInput()
	