filename = '252022.txt'
file = open("inputs/"+filename, 'r')

snafuDict = {"-": -1, "=": -2}
decimalSum = 0
def to_balanced_quinary(decimal_number):
    if decimal_number == 0:
        return '0'

    result = ''
    base = 5

    while decimal_number != 0:
        remainder = decimal_number % base
        decimal_number //= base

        if remainder > base // 2:
            remainder -= base
            decimal_number += 1
        if remainder == -2:
            remainder = "="
        elif remainder == -1:
            remainder = "-"
        result = str(remainder) + result

    return result

for line in file.readlines():
    line = line.rstrip()
    line = list(line)[::-1]
    currMultiplier = 1

    decimalValue = 0

    for num in line:
        if num not in snafuDict:
            decimalValue += int(num) * currMultiplier
        else:
            decimalValue += snafuDict[num] * currMultiplier
        currMultiplier *= 5
    decimalSum += decimalValue
print(decimalSum)
snafu = ""
currMultiplier = 1
while (currMultiplier <= decimalSum):
    currMultiplier *= 5
currMultiplier//=5

print(to_balanced_quinary(decimalSum))
