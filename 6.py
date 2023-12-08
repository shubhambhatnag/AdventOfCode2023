filename = '6.txt'
file = open("inputs/"+filename, 'r')


races = {}
lines = file.readlines()
times = lines[0].rstrip().split(" ")[1:]
#delete all '' from times
while ('' in times):
    times.remove('')

distances = lines[1].rstrip().split(" ")[1:]
while ('' in distances):
    distances.remove('')
print(times)
print(distances)

# map each time to each distance

races = []

for i in range(len(times)):
    races.append((int(times[i]), int(distances[i])))

total = 1
for race in races:
    time = race[0]
    record = race[1]
    workingTimes = 0
    for i in range(time + 1):
        if i * (time - i) > record:
            workingTimes += 1
    print(workingTimes)
    total *= workingTimes

print(total)