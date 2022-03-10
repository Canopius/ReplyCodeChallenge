def processInput(toProcess, caseNo):
	# Line by line
	output = True

	x = list(map(int,toProcess.strip().split(" ")))
	
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
	