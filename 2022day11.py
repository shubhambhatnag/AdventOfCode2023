#filename = '112022.txt'
#file = open("inputs/"+filename, 'r')

monkeyInspection = [0,0,0,0,0,0,0,0]

monkeyInvs = [[54, 98, 50, 94, 69, 62, 53, 85],[71, 55, 82],[77, 73, 86, 72, 87],[97, 91],[78, 97, 51, 85, 66, 63, 62], [88], [87, 57, 63, 86, 87, 53], [73, 59, 82, 65]]



for s in range(10000):
    print(s)
    for monkey in range(len(monkeyInvs)):
        if monkeyInvs[monkey] == []:
            
            continue
        
        for item in range(len(monkeyInvs[monkey])):
            monkeyInspection[monkey] += 1
            if (monkey == 0):
                monkeyInvs[monkey][item] *= 13
                monkeyInvs[monkey][item] %= 10 
                #print(monkeyInvs[monkey][item])
                #newVal = int(monkeyInvs[monkey][item] / 3)
                #monkeyInvs[monkey][item] = int(monkeyInvs[monkey][item] / 3)
                if (monkeyInvs[monkey][item] % 3 == 0):

                    monkeyInvs[2].append(monkeyInvs[monkey][item])
                    
                else:
                    monkeyInvs[1].append(monkeyInvs[monkey][item])
                

            elif (monkey == 1):
                monkeyInvs[monkey][item] += 2
                monkeyInvs[monkey][item] %= 10 
                #monkeyInvs[monkey][item] = int(monkeyInvs[monkey][item] / 3)
                if (monkeyInvs[monkey][item] % 13 == 0):
                    monkeyInvs[7].append(monkeyInvs[monkey][item])
                else:
                    monkeyInvs[2].append(monkeyInvs[monkey][item])
            
            elif (monkey == 2):
                monkeyInvs[monkey][item] += 8
                monkeyInvs[monkey][item] %= 10 
                #monkeyInvs[monkey][item] = int(monkeyInvs[monkey][item] / 3)
                if (monkeyInvs[monkey][item] % 19 == 0):
                    monkeyInvs[4].append(monkeyInvs[monkey][item])
                else:
                    monkeyInvs[7].append(monkeyInvs[monkey][item])

            elif (monkey == 3):
                monkeyInvs[monkey][item] += 1
                monkeyInvs[monkey][item] %= 10 
                #monkeyInvs[monkey][item] = int(monkeyInvs[monkey][item] / 3)
                if (monkeyInvs[monkey][item] % 17 == 0):
                    monkeyInvs[6].append(monkeyInvs[monkey][item])
                else:
                    monkeyInvs[5].append(monkeyInvs[monkey][item])
            elif (monkey == 4):
                monkeyInvs[monkey][item] *= 17
                monkeyInvs[monkey][item] %= 10 
                #monkeyInvs[monkey][item] = int(monkeyInvs[monkey][item] / 3)
                if (monkeyInvs[monkey][item] % 5 == 0):
                    monkeyInvs[6].append(monkeyInvs[monkey][item])
                else:
                    monkeyInvs[3].append(monkeyInvs[monkey][item])
            elif (monkey == 5):
                monkeyInvs[monkey][item] += 3
                monkeyInvs[monkey][item] %= 10 
                #monkeyInvs[monkey][item] = int(monkeyInvs[monkey][item] / 3)
                if (monkeyInvs[monkey][item] % 7 == 0):
                    monkeyInvs[1].append(monkeyInvs[monkey][item])
                else:
                    monkeyInvs[0].append(monkeyInvs[monkey][item])
            elif (monkey == 6):
                monkeyInvs[monkey][item] *= monkeyInvs[monkey][item]
                monkeyInvs[monkey][item] %= 10 
                #monkeyInvs[monkey][item] = int(monkeyInvs[monkey][item] / 3)
                if (monkeyInvs[monkey][item] % 11 == 0):
                    monkeyInvs[5].append(monkeyInvs[monkey][item])
                else:
                    monkeyInvs[0].append(monkeyInvs[monkey][item])
            elif (monkey == 7):
                monkeyInvs[monkey][item] += 6
                monkeyInvs[monkey][item] %= 10 
                #monkeyInvs[monkey][item] = int(monkeyInvs[monkey][item] / 3)
                if (monkeyInvs[monkey][item] % 2 == 0):
                    monkeyInvs[4].append(monkeyInvs[monkey][item])
                else:
                    monkeyInvs[3].append(monkeyInvs[monkey][item])
        monkeyInvs[monkey] = []

biggest = max(monkeyInspection)
monkeyInspection.remove(biggest)
secondBiggest = max(monkeyInspection)

print(biggest * secondBiggest)
