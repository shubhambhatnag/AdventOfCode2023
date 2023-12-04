filename = '142022.txt'
file = open("inputs/"+filename, 'r')
import matplotlib.pyplot as plt
walls = set()
highest_x = None
lowest_x = None
highest_y = None
for line in file.readlines():
    line = line.rstrip()


    line = line.split(' -> ')
    
    
    for i in range(len(line)):
        line[i] = line[i].split(',')
        for j in range(len(line[i])):
            line[i][j] = int(line[i][j])

    #print(line)
    for point in range(len(line) - 1):
        point1 = line[point]
        point2 = line[point + 1]
   
        if (line[point][0] == line[point + 1][0]):
       
            for y in range(min(point1[1], point2[1]), max(point1[1], point2[1]) + 1):
                if (highest_y == None or y > highest_y):
                    highest_y = y
                
                walls.add((line[point][0], y))
        else:
            for x in range(min(point1[0], point2[0]), max(point1[0], point2[0]) + 1):
                if (highest_x == None or y > highest_x):
                    highest_x = x
                if (lowest_x == None or y < lowest_x):
                    lowest_x = x
                walls.add((x, line[point][1]))
sandCount = 0
limit = False

while (not limit):
    rest = False
    
    sandPos = (500, 0)
    while (not rest):
   
        if ((sandPos[0], sandPos[1] + 1) in walls):
            if ((sandPos[0] - 1, sandPos[1] + 1) in walls):
                if ((sandPos[0] + 1, sandPos[1] + 1) in walls):
                    rest = True
                    if (sandPos[1] == 0):
                        limit = True
                    walls.add(sandPos)
                    sandCount += 1
                else:
                    sandPos = (sandPos[0] + 1, sandPos[1] + 1)
            else:
                sandPos = (sandPos[0] - 1, sandPos[1] + 1)
        else:
            sandPos = (sandPos[0], sandPos[1] + 1)

print(sandCount)
            



    