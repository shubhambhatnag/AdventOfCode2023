filename = '9.txt'
file = open("inputs/"+filename, 'r')
lines = file.readlines()
extrapolations = []


def extrapolate(series):
    #print(series)
    #Check if series is all 0

    if len(set(series)) == 1 and series[0] == 0:
        return series[0]
    
    return(series[0] - extrapolate([series[i+1] - series[i] for i in range(len(series)-1)]))

for line in lines:
    line = line.rstrip()
    series = line.split(" ")
    #Conv all elements to int
    series = list(map(int, series))
    extrapolations.append(extrapolate(series))
print(sum(extrapolations))