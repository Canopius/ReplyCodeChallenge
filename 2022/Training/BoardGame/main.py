from math import ceil

def processInput(toProcess, caseNo):
    output = True
	# Line by line
    x = list(map(int,toProcess.strip().split(" ")))
    
    # Health = [0], Attack = [1], Defence = [2]
    p1 = x[0:3]
    p2 = x[3::]

    p1HealthLossPerTurn = p2[1] - p1[2]
    p2HealthLossPerTurn = p1[1] - p2[2]

    if p1HealthLossPerTurn == 0:
        p1HealthLossPerTurn = -1
    
    if p2HealthLossPerTurn == 0:
        p2HealthLossPerTurn = -1

    p1UntilDeath = ceil(p1[0] / p1HealthLossPerTurn)
    p2UntilDeath = ceil(p2[0] / p2HealthLossPerTurn)

    if p1UntilDeath < 0 and p2UntilDeath > 0:
        output = 1
    elif p1UntilDeath > 0 and p2UntilDeath < 0:
        output = 2
    elif p2UntilDeath < 0 and p2UntilDeath < 0:
        output = 0
    elif p2UntilDeath == p1UntilDeath:
        output = 0
    elif p1UntilDeath > p2UntilDeath:
        output = 1
    elif p2UntilDeath > p1UntilDeath:
        output = 2
    else:
        print("Case unsolved: ", p1, " ", p2)
        

    
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
	