filename = '10.txt'
file = open("inputs/"+filename, 'r')
lines = file.readlines()
inp = []
graph = {}



for line in lines:
    line = line.rstrip()

    inp.append(list(line))
    


#Locate S in inp

def spread(x, y):
    global graph
    global inp
    if (x,y) in graph:
        return
    if inp[x][y] == '.':
        return
    elif inp[x][y] == "S":
        
        if (x-1 >= 0):
            
            if inp[x-1][y] == "-" or inp[x-1][y] == "7" or inp[x-1][y] == "J":
                graph[(x,y)].append((x-1,y))
                spread(x-1,y)
        if (x+1 < len(inp[0])):
            
            if inp[x+1][y] == "-" or inp[x+1][y] == "L" or inp[x+1][y] == "F":
                graph[(x,y)].append((x+1,y))
                spread(x+1,y)
        if (y-1 >= 0):
            if inp[x][y-1] == "|" or inp[x][y-1] == "7" or inp[x][y-1] == "F":
                graph[(x,y)].append((x,y-1))
                spread(x,y-1)
        if (y+1 < len(inp[x])):
            if inp[x][y+1] == "|" or inp[x][y+1] == "J" or inp[x][y+1] == "L":
                graph[(x,y)].append((x,y+1))
                spread(x,y+1)
    elif inp[x][y] == "|":
        if (y-1 >= 0):
            graph[(x,y)].append((y-1,y))
            spread(x-1,y)
        if (y+1 < len(inp)):
            graph[(x,y)].append((y+1,y))
            spread(y+1,y)
    elif inp[x][y] == "-":
        if (x-1 >= 0):
            graph[(x,y)].append((x-1,y))
            spread(x-1,y)
        if (x+1 < len(inp[0])):
            graph[(x,y)].append((x+1,y))
            spread(x+1,y)
    elif inp[x][y] == "L":
        if (x+1 < len(inp[0])):
            graph[(x,y)].append((x+1,y))
            spread(x+1,y)
        if (y-1 >= 0):
            graph[(x,y)].append((y-1,y))
            spread(x-1,y)
    #J is a 90-degree bend connecting north and west.
    elif inp[x][y] == "J":
        if (x-1 >= 0):
            graph[(x,y)].append((x-1,y))
            spread(x-1,y)
        if (y-1 >= 0):
            graph[(x,y)].append((y-1,y))
            spread(x,y-1)
    #7 is a 90-degree bend connecting south and west.
    elif inp[x][y] == "7":
        if (x-1 >= 0):
            graph[(x,y)].append((x-1,y))
            spread(x-1,y)
        if (y+1 < len(inp)):
            graph[(x,y)].append((x,y+1))
            spread(x,y+1)
    elif inp[x][y] == "F":
        if (x+1 < len(inp[0])):
            graph[(x,y)].append((x+1,y))
            spread(x+1,y)
        if (y+1 < len(inp)):
            graph[(x,y)].append((x,y+1))
            spread(x,y+1)
    


#test

for i in range(len(inp)):
    for j in range(len(inp[i])):
        if inp[i][j] == "S":
            start = (i, j)
graph = {}

spread(start[0], start[1])

print(graph)