filename = '4.txt'
file = open("inputs/"+filename, 'r')


pointSum = 0

scratchCards = {}



for line in file.readlines():
    found = 0
    line = line.rstrip()
    winning = line.split("|")[0].split(" ")
    current = line.split("|")[1].split(" ")

    winning = [x for x in winning if x != '']
    current = [x for x in current if x != '']
    #print(winning)
    cardID = int(winning[1][:len(winning[1]) - 1])
    #print(cardID)
    winning = winning[2:len(winning)]

    scratchCards[cardID] = [winning, current,[]]
    #Remove all '' from winning and current



cardList = list(scratchCards.keys())

for card in cardList:
    if (scratchCards[card][2] == []):
        #print(card)
        #print(cardList)
        winning = scratchCards[card][0]
        current = scratchCards[card][1]
        #print(winning)
        #print(current)
        found = 0

        for num in current:
            if (num in winning):
                found += 1
        cardWinnings = []
        while (found != 0):
            #print(found)
            cardList.append(card + found)
            cardWinnings.append(card + found)
            #print(card + found)
            found -= 1
        scratchCards[card][2] = cardWinnings
    else:
        #Append contents of scratchCards[card][2] to cardList
        cardList += scratchCards[card][2]
print(len(cardList))

    

#Count how much of each number is in cardList


    
    

#print(pointSum)
    
    