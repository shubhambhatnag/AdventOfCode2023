filename = '122022.txt'
file = open("inputs/"+filename, 'r')

elevations = []

for line in file.readlines():
    elevations.append(list(line.rstrip()))
#turn 'a' into '0', 'b' into '1', etc.
for line in range(len(elevations)):
    for char in range(len(elevations[line])):
        if (elevations[line][char] not in ["S", "E"]):
            elevations[line][char] = ord(elevations[line][char]) - 97
def checkValidPath(line, char, lineModifier, charModifier):

    try:
        elevation = elevations[line][char]
        neighbor = elevations[line+lineModifier][char+charModifier]
    
        if (neighbor == "S"):
            neighbor = 0
        elif (neighbor == "E"):
            neighbor = 25

        if (elevation == "S"):
            elevation = 0
        elif (elevation == "E"):
            elevation = 25
        if (line+lineModifier < 0 or char+charModifier < 0):
            return False
    
        if ((elevation >= neighbor) or (elevation + 1 == neighbor)):
            return True
        else:
            return False
    except:
        return False
    
graph = {}
startings = []
ending = ()

for line in range(len(elevations)):
    for char in range(len(elevations[line])):
        graph[(line, char)] = []
        for modifiers in [(0,1),(0,-1),(1,0),(-1,0)]:
            if (checkValidPath(line, char, modifiers[0], modifiers[1])):
                graph[(line, char)].append((line+modifiers[0], char+modifiers[1]))
                if (elevations[line][char] == "S" or elevations[line][char] == 0):
                    if ((line,char) not in startings):
                        startings.append((line, char))
                elif (elevations[line][char] == "E"):
                    ending = (line, char)

            

def getClosestVertex(distances, finishedSet):
    closestVertex = None
    minDistance = 1000000000000

    for vertex in distances:
        if (distances[vertex] < minDistance and vertex not in finishedSet):
            closestVertex = vertex
            minDistance = distances[vertex]

    return closestVertex
#print(graph)

minimumDistance = None

for starting in startings:
    print(starting)
    finishedSet = set()

    distances = {}

    predecessors = {}


    for vertex in graph:
        distances[vertex] = 100000000000000000000

    distances[starting] = 0

    while (len(finishedSet) != len(graph)):
        currVertex = getClosestVertex(distances, finishedSet)
        if (currVertex == None):
            break
        finishedSet.add(currVertex)
        
        for neighbor in graph[currVertex]:
            if (neighbor not in finishedSet):
                if (distances[currVertex] + 1 < distances[neighbor]):
                    distances[neighbor] = distances[currVertex] + 1
                    predecessors[neighbor] = currVertex

    if (minimumDistance == None or distances[ending] < minimumDistance):
        minimumDistance = distances[ending]

print(minimumDistance)