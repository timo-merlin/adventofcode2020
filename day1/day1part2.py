f = open("input.txt", "r")
target = 2020
entries = []

for line in f:
    entries.append(int(line.rstrip()))

entries.sort()
reverse = entries[:]
reverse.reverse()

found = False
for x in entries:
    for y in entries:
        for z in reverse:
            if (x+y+z == target):
                found = True
                break
            elif (x+y+z < target):
                break

        if found:
            break
    if found:
        print("{} + {} + {} = 2020 // Product: {}".format(x,y,z,x*y*z))
        break