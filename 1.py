filename = '1.txt'
file = open("inputs/"+filename, 'r')
total = 0
with file:
    total = 0

    for line in file.readlines():
        new_line = line.rstrip().lower()
        num_dict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9", "zero": "0"}
        numList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"]
        first = ""
        last = ""
        lineList = (line)

        firstPointer = 0

        while firstPointer <= len(lineList):
            selection = lineList[:firstPointer]
            for num in numList:
                if num in selection:

                    if (num in num_dict):
                        first = num_dict[num]
                    else:
                        first = num
                    break
            if (first != ""):
                break
            firstPointer += 1
        lastPointer = len(lineList) - 1
        while lastPointer >= 0:
            selection = lineList[lastPointer:]
            for num in numList:
                if num in selection:
                    if (num in num_dict):
                        last = num_dict[num]
                    else:
                        last = num
                    break
            if (last != ""):
                break
            lastPointer -= 1
        total += int(first + last)
    print(total)
                