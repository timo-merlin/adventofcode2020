import math
f = open("./input.txt", "r")
lines = []
max = 0

for line in f:
    lines.append(line.rstrip())

def recursio(min, max, s):
    if (len(s) == 1):
        if (s == "F") or (s == "L"):
            return min
        else:
            return max
    if (s[0] == "F") or (s[0] == "L"):
        return recursio(min, min + int((max-min)/2), s[1:])
    return recursio(min + math.ceil((max-min)/2), max, s[1:])

for boarding_pass in lines:
    id = (recursio(0,127,boarding_pass[:7]) * 8) + recursio(0, 7, boarding_pass[-3:])
    if id > max:
        max = id

print("The highest id is: {}".format(max))