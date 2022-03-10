def findNearest(mousePos, lastPos, targets):
	nearestDist = 10**1000 # Some large number
	nearestDistX = 10**1000
	nearestDistY = 10**1000
	nearest = []
	f = 0
	
	for i in range(len(targets)):
		distX = (targets[i][0] - mousePos[0])
		distY = (targets[i][1] - mousePos[1])
		print("Be: ", targets[i])
		if ((targets[i][0] == lastPos[0]) and (targets[i][1] == lastPos[1])) or len(targets[i]) <= 0:
			print(targets[i], "hsdf")
			pass
		else:
			dist = abs(distY^2 - distX^2)
			print("Op: ", dist, targets[i])
			if nearestDist == dist:
				print(":::", nearest)
				if nearest[0] - mousePos[0] < distX:
					continue
				elif nearest[0] - mousePos[0] == distX:
					if nearest[1] - mousePos[1] < distX:
						continue

			
			if dist < nearestDist:
				nearestDist = dist
				nearestDistX = distX
				nearestDistY = distY
				nearest = targets[i]
				f = i

	print("Nearest: ", nearest)

	return nearest, nearestDist, f

def processInput(toProcess, targets, caseNo):
	# Line by line
	output = 0
	oldi = 0

	x = list(map(int,toProcess.strip().split(" ")))

	#Targets[0] = start

	mousePos = targets[0]
	lastPos = targets[0]

	
	while len(targets) > 0:
		near, dist, i = findNearest(mousePos, lastPos, targets)
		output += dist
		

		if mousePos[2] == 0:
			targets.remove(targets[oldi])

		oldi = i

		mousePos = near
		near[2] -= 1
		lastPos = mousePos

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
			enemyNo = list(map(int,line.strip().split(" ")))[1]
			enemyInfo = []
			for i in range(enemyNo):
				enemyInfo.append(list(map(int,f.readline().strip().split(" "))))

			processInput(line, enemyInfo, caseNo)
			caseNo += 1
if __name__ == "__main__":
	getInput()
	