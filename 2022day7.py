filename = '72022.txt'
file = open("inputs/"+filename, 'r')

with file:
    fileSystem = {"/":[None, []]}
    currentDir = None

    for line in file.readlines():
        line = line.rstrip().split(" ")
        if (line[0] == "$"):
            if (line[1] == "cd"):
                if (line[2] == ".."):
                    currentDir = fileSystem[currentDir][0]
                elif (line[2] == "/"):
                    currentDir = "/"
                else:
                    currentDir = currentDir+line[2]
        else:
            if (line[0] == "dir"):
                fileSystem[currentDir][1].append(currentDir+line[1])
                fileSystem[currentDir+line[1]] = [currentDir, []]
            else:
                fileSystem[currentDir][1].append(int(line[0]))
    
    def getSize(dir):
        size = 0
        for file in fileSystem[dir][1]:
            if (type(file) == int):
                size += file
            else:
                size += getSize(file)
        return size
    
    neededSize = 30000000 - (70000000 - getSize("/"))

    smallestFound = None
    for directory in fileSystem:
        if (getSize(directory) >= neededSize):
            if (smallestFound == None or getSize(directory) < getSize(smallestFound)):
                smallestFound = directory
            
    #print(getSize("d"))
    print(getSize(smallestFound))