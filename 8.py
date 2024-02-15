filename = '8.txt'
file = open("inputs/"+filename, 'r')
lines = file.readlines()

instructions = list(lines[0].rstrip())
steps = 0
print(lines)
graph = {}
for line in lines[2:]:
    line = line.rstrip().split(" = ")
    graph[line[0]] = line[1][1:-1].split(", ")

def checkNodes(currs):
    for curr in currs:
        if curr[-1] != 'Z':
            return False
    return True
currs = []

for key in graph.keys():
    if key[-1] == 'A':
        currs.append(key)
print(currs)
while not checkNodes(currs):
    
    for instruction in instructions:
        if (currs[0][-1] == 'Z'):
            print(currs[0])
        if (checkNodes(currs)):
            break
        if instruction == 'L':
            for i in range(len(currs)):
                currs[i] = graph[currs[i]][0]
           
        elif instruction == 'R':
            for i in range(len(currs)):
                currs[i] = graph[currs[i]][1]
        steps += 1
print(steps)

