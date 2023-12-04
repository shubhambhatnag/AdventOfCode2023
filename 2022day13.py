filename = '132022.txt'
import ast
file = open("inputs/"+filename, 'r')

packets = []
key1 = [[[[2]]]]
key2 = [[[[6]]]]
for line in file.readlines():
    line = line.rstrip()
    if (line != ""):
        packets.append(ast.literal_eval(line))        
packets += [[2]],[[6]]
#print(packets)
def checkPair(first, second):
    global key1
    global key2
    left = 0
    right = 0

    #While loop until either left is equal to length of first or right is equal to the longth of second
    while (left != len(first) and right != len(second)):
        if (type(first[left]) == int and type(second[right]) == int):
            if (first[left] < second[right]):
                return True
            elif (first[left] > second[right]):
                
                return False   
        elif (type(first[left]) == list and type(second[right]) == list):
            if (checkPair(first[left], second[right]) == True):
                return True
            elif (checkPair(first[left], second[right]) == False):
                
                return False
        else:
            if (type(first[left]) == int):
                if (first) == key1:
                    key1 = [key1]
                elif (first) == key2:
                   
                    key2 = [key2]
                first[left] = [first[left]]
            else:
                if (second) == key1:
                    key1 = [key1]
                elif (second) == key2:
                    
                    key2 = [key2]
                second[right] = [second[right]]
            if (checkPair(first[left], second[right]) == True):
                return True
            elif (checkPair(first[left], second[right]) == False):
                #print("here")
                return False
        left += 1
        right += 1
    if (len(first) == len(second)):
        #print("here")
        return None
    else: 
        #print("here")
        return len(first) < len(second)


n = len(packets)

swapped = False




for i in range(n-1):

    for j in range(0, n-i-1):

        if checkPair(packets[j],packets[j + 1]):
            swapped = True
            packets[j], packets[j + 1] = packets[j + 1], packets[j]
        
    if not swapped:
        # if we haven't needed to make a single swap, we 
        # can just exit the main loop.
        break

packets = packets[::-1]
#for packet in packets:
 #   print(packet)
print((packets.index(key1)+1)*(packets.index(key2)+1))