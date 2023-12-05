filename = '5.txt'
file = open("inputs/"+filename, 'r')

seeds = []
lines = file.readlines()


parsed=lines[0].rstrip().split(" ")
mapData = []


parsed = parsed[1:]

#Turn parsed into pairs of ints

for i in range(len(parsed)):
    print(len(parsed) - i)
    if (i % 2 == 0):
        for j in range(int(parsed[i+1])):
            seeds.append([int(parsed[i])+j])

        


print(seeds)
print(len(seeds))
maps = ["seed-to-soil","soil-to-fertilizer","fertilizer-to-water","water-to-light","light-to-temperature","temperature-to-humidity","humidity-to-location"]

for currMap in range(len(maps)):
    print("Map: " + maps[currMap])
    index = lines.index(maps[currMap] + " map:\n")
    currLine = index + 1
    while (lines[currLine] != "\n"):

        ranges = lines[currLine].rstrip().split(" ")
        destRange = int(ranges[0])
        sourceRange = int(ranges[1])
        rangeLength = int(ranges[2])
        # if (currMap == 0):
        #     for seedRange in seedRanges:
        #         seed_start, seed_end = seedRange[0], seedRange[0] + seedRange[1]
        #         source_start, source_end = sourceRange, sourceRange + rangeLength

        #         overlap_start = max(seed_start, source_start)
        #         overlap_end = min(seed_end, source_end)

        #         # Check if there is an actual overlap
        #         if overlap_start < overlap_end:
        #             for i in range(overlap_start, overlap_end):
        #                 seeds.append([i, destRange+(i-sourceRange)])
        #                 break


                
        # else:
        for data in seeds:
            if (data[-1] in range(sourceRange, sourceRange + rangeLength)):
                if (len(data) == currMap + 1):
                    data.append(destRange+(data[-1]-sourceRange))
        currLine += 1

        if (currLine >= len(lines)):
            break
    for data in seeds:
        if len(data) == currMap + 1:
            data.append(data[-1])


smallestLocation = None

for data in seeds:
    if (smallestLocation == None or data[-1] < smallestLocation):
        smallestLocation = data[-1]

#Create new file smallest.txt and write this int to it
print(smallestLocation)


        