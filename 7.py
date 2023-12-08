filename = '7.txt'
file = open("inputs/"+filename, 'r')
handDict = {}
for line in file.readlines():
    line = line.rstrip().split(" ")
    handDict[line[0]] = int(line[1])

hands = list(handDict.keys())
order = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
def getType(hand):
    #Check for 5 of a kind
    for card in order:
        if hand.count(card) + hand.count("J") >= 5:
            return 7
    
    #check for 4 of a kind

    for card in order:
        if hand.count(card) + hand.count("J") >= 4:
            return 6
    
    #check for full house (3 of a kind and a pair)
    three = False
    two = False
    for card in order:
        if hand.count(card) + hand.count("J") >= 3:
            three = True
        if hand.count(card) + hand.count("J") >= 2:
            two = True
    if three and two:
        return 5
    
    #check for 3 of a kind
    if three:
        return 4

    #Check for 2 pair
    pairs = 0
    for card in order:
        if hand.count(card) + hand.count("J") >= 2:
            pairs += 1
    if pairs == 2:
        return 3
    
    #Check for 1 pair
    if pairs == 1:
        return 2
    
    #Check for high card
    return 1
    


nameDict = {7:"Five of a Kind", 6:"Four of a Kind", 5:"Full House", 4:"Three of a Kind", 3:"Two Pair", 2:"One Pair", 1:"High Card"}
def compareHands(first, second):
    if getType(first) > getType(second):
        return True
    elif getType(first) < getType(second):
        return False
    else:
        for i in range(len(first)):
            if order.index(first[i]) > order.index(second[i]):
                return True
            elif order.index(first[i]) < order.index(second[i]):
                return False
    
for hand in hands:
    print(hand,nameDict[getType(hand)])

n = len(hands)

# Traverse through all handsay elements
for i in range(n):
# Last i elements are already in place, so we don't need to check them
    for j in range(0, n - i - 1):
        # Swap if the element found is greater than the next element
        if compareHands(hands[j], hands[j + 1]):
            hands[j], hands[j + 1] = hands[j + 1], hands[j]

totalWinnings = 0
for index in range(len(hands)):
    totalWinnings += handDict[hands[index]] * (index + 1)

print(totalWinnings)