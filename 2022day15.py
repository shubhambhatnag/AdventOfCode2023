filename = '152022.txt'
file = open("inputs/"+filename, 'r')


def manhattan(p1,p2):
    return(abs(p2[0] - p1[0]) + abs(p2[1] - p1[1]))


sensors = {}
leftBound = None
rightBound = None
beacons = []
for line in file.readlines():
    line = line.rstrip().split(" ")
    #print(line)
    sensorX = int(line[2][:len(line[2])-1].split("=")[1])
    sensorY = int(line[3][:len(line[3])-1].split("=")[1])

    beaconX = int(line[8][:len(line[8])-1].split("=")[1])
    beaconY = int(line[9].split("=")[1])
    beacons.append((beaconX, beaconY))
    sensors[(sensorX, sensorY)] = manhattan((sensorX, sensorY), (beaconX, beaconY))
    #print(sensorX - sensors[(sensorX, sensorY)])
    if (leftBound == None or (sensorX - sensors[(sensorX, sensorY)] < leftBound)):
        leftBound = sensorX - sensors[(sensorX, sensorY)]

    if (rightBound == None or sensorX + sensors[(sensorX, sensorY)] > rightBound):
        rightBound = sensorX + sensors[(sensorX, sensorY)]

print(sensors)
impossible = 0
for x in range(leftBound, rightBound):
    coordinate = (2000000, x)
    for sensor in sensors:
        if (manhattan(coordinate, sensor) <= sensors[sensor] and coordinate not in beacons):
            impossible += 1
            break
print(impossible)
