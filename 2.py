filename = '2.txt'
file = open("inputs/"+filename, 'r')

with file:
    powerCount = 0
    for line in file.readlines():
        colorCount = {"red":-1, "green":-1, "blue":-1}
        game = line.rstrip().split(": ")[1]
        for colorSet in game.split("; "):
            for color in colorSet.split(", "):
                turn = color.split(" ")
                if (int(turn[0]) > colorCount[turn[1]]):
                    colorCount[turn[1]] = int(turn[0])
        
        powerCount += int(colorCount["red"] * colorCount["green"] * colorCount["blue"])
    print(powerCount)