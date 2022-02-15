def processInput(toProcess, caseNo):
	# Line by line

	output = True
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
			processInput(line, caseNo)
			caseNo += 1

if __name__ == "__main__":
	getInput()
	