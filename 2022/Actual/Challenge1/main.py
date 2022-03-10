def processInput(toProcess, meta, caseNo):
	# Line by line
	output = 0
	
	data = list(map(int,meta.strip().split(" ")))
	meta = list(map(int,toProcess.strip().split(" ")))
	
	maxDays = meta[1]

	data.sort()

	online = []

	for i in range(len(data)):
		online.append(range(1, maxDays+1, data[i]))

	ans = set(online[0])

	for i in range(1, len(online)):
		ans = ans.intersection(online[i])

	
	output = len(list(ans))
	
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
			line2 = f.readline()
			processInput(line, line2, caseNo)
			caseNo += 1

if __name__ == "__main__":
	getInput()
	