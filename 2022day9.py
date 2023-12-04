filename = '92022.txt'
file = open("inputs/"+filename, 'r')


pieces = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

def checkDiagonal(head,tail):
    if (head[0]+1 == tail[0] and head[1]+1 == tail[1]):
        return True
    if (head[0]+1 == tail[0] and head[1]-1 == tail[1]):
        return True
    if (head[0]-1 == tail[0] and head[1]+1 == tail[1]):
        return True
    if (head[0]-1 == tail[0] and head[1]-1 == tail[1]):
        return True
    return False
def checkAdjacent(tail
                  ,head):
    if (head[0]+1 == tail[0] and head[1] == tail[1]):
        return True
    if (head[0]-1 == tail[0] and head[1] == tail[1]):
        return True
    if (head[0] == tail[0] and head[1]+1 == tail[1]):
        return True
    if (head[0] == tail[0] and head[1]-1 == tail[1]):
        return True
    return False
foundSet = set()
foundSet.add(tuple(pieces[-1]))
#print(found)



def newPosition(head, tail):
    if (head[0] == tail[0]):
        if (head[1] - tail[1] > 1):
            tail[1] += 1
        elif (head[1] - tail[1] < -1):
            tail[1] -= 1
    elif (head[1] == tail[1]):
        if (head[0] - tail[0] > 1):
            tail[0] += 1
        elif (head[0] - tail[0] < -1):
            tail[0] -= 1
    elif (not checkDiagonal(head, tail)):
        # for i in [-1,1]:
        #     for j in [-1,1]:
        #         if (checkAdjacent(head,[tail[0]+i, tail[1]+j])):
        #             tail[0] += i
        #             tail[1] += j
        #             break


        dist = abs(head[0] - tail[0]) + abs(head[1] - tail[1])

        options = [[1, 1], [1, -1], [-1, 1], [-1, -1]]

        # Try each diagonal option

        for dx, dy in options:

            # Calculate hypothetic new position
            newX = tail[0] + dx 
            newY = tail[1] + dy
            
            # Compute hypothetical distance
            newDist = abs(newX - head[0]) + abs(newY - head[1])

            # Check if this option gets us closer 
            if newDist < dist:

                # Update tail position 
                tail[0] = newX 
                tail[1] = newY
                dist = newDist # update saved distance

                # Only process one option 
                break
    return tail


for line in file.readlines():
    direction = line.rstrip().split(" ")[0]
    count = int(line.rstrip().split(" ")[1])
    
    while (count > 0):
        
        if (direction == "U"):
            pieces[0][1] += 1
        elif (direction == "D"):
            pieces[0][1] -= 1
        elif (direction == "L"):
            pieces[0][0] -= 1
        elif (direction == "R"):
            pieces[0][0] += 1
                
        count -= 1
        
        #Keep tail at most 1 away from head
        for piece in range(len(pieces)-1):
            pieces[piece+1] = newPosition(pieces[piece], pieces[piece+1])
                    
        foundSet.add(tuple(pieces[-1]))

print(len(foundSet))

            
            