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
    for y in reverse:
        if (x+y == target):
            found = True
            break
        elif (x+y < target):
            break

    if found:
        print("{} + {} = 2020 // Product: {}".format(x,y,x*y))
        break