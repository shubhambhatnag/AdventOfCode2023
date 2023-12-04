filename = '102022.txt'
file = open("inputs/"+filename, 'r')

signalStrength = 0
X = 1
cycle = 1
cycleChecks = [20,60,100,140,180,220]
cyclePos = []
for line in file.readlines():
    #print(cyclePos)
    line = line.rstrip()
    line = line.split(" ")
    toAdd = 0
    if (line[0] == "noop"):
        cyclePos.append(X)
        cycle += 1
        
    elif (line[0] == "addx"):
        toAdd = int(line[1])
        
        cyclePos.append(X)
        cyclePos.append(X)
        X += toAdd
        
        cycle += 2
        
    if (cycleChecks != []):
        if (cycleChecks[0] < cycle):
            signalStrength += (X-toAdd) * cycleChecks[0]
            cycleChecks.pop(0)
        elif (cycleChecks[0] == cycle):
            signalStrength += X * cycleChecks[0]
            cycleChecks.pop(0)
line = ""


for i in range(40):
    if (abs(i-cyclePos[i]) <= 1):
        
        line += ("#")
    else:
        line += (".")
print(line)
line = ""
for i in range(40,80):
    if (abs((i % 40)-cyclePos[i]) <= 1):
        
        line += ("#")
    else:
        line += (".")
print(line)
line = ""
for i in range(80,120):
    if (abs((i % 40)-cyclePos[i]) <= 1):
        
        line += ("#")
    else:
        line += (".")
print(line)
line = ""
for i in range(120,160):
    if (abs((i % 40)-cyclePos[i]) <= 1):
        
        line += ("#")
    else:
        line += (".")
print(line)

line = ""
for i in range(160,200):
    if (abs((i % 40)-cyclePos[i]) <= 1):
        
        line += ("#")
    else:
        line += (".")
print(line)

line = ""
for i in range(200,240):
    if (abs((i % 40)-cyclePos[i]) <= 1):
        
        line += ("#")
    else:
        line += (".")
print(line)


#print(cyclePos)
# #print(cyclePos)
