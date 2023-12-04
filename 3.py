filename = '3.txt'
file = open("inputs/"+filename, 'r')

schematic = []

totalSum = 0

for line in file.readlines():
    schematic.append(list(line.rstrip()))

def checkSymbol(lineModifier, charModifier):
    try:
        if ((not schematic[line+lineModifier][char+charModifier].isdigit()) and schematic[line+lineModifier][char+charModifier] != "."):
            return True
        else:
            return False
    except:
        return False
currInt = ""
foundSymbol = False
gearLocation = None
gearRatios = {}
for line in range(len(schematic)):
    if (currInt != ""):
        if (foundSymbol):
            
            totalSum += int(currInt)
    currInt = ""
    foundSymbol = False
    for char in range(len(schematic[line])):
        if (schematic[line][char].isdigit()):
            currInt += schematic[line][char]
            #Check surrounding spaces for a symbol
            if (not foundSymbol):
                for (lineModifier, charModifier) in [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]:
                    if (checkSymbol(lineModifier, charModifier)):
                        
                        foundSymbol = True
                        if (schematic[line+lineModifier][char+charModifier] == "*"):
                            gearLocation = (line+lineModifier, char+charModifier)
                        break
        else:
            if (currInt != ""):
                if (foundSymbol):
                    #print(currInt)
                    totalSum += int(currInt)
                    if (gearLocation != None):
                        if (gearLocation in gearRatios):
                            
                            gearRatios[gearLocation][1] *= int(currInt)
                            gearRatios[gearLocation][0] += 1
                        else:
                            gearRatios[gearLocation] = [1, int(currInt)]
                            
                    
                    gearLocation = None
                    print(currInt)
                    foundSymbol = False
                    currInt = ""
                else:
                    currInt = ""
                    gearLocation = None
            else:
                foundSymbol = False
                currInt = ""
                gearLocation = None
                    

print(totalSum)
ratioSum = 0
print(gearRatios)
for gear in gearRatios:
    if (gearRatios[gear][0] == 2):
        ratioSum += gearRatios[gear][1]
print(ratioSum)