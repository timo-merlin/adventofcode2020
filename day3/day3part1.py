f = open("./input.txt", "r")
lines = []
x = 0
treecount = 0

for line in f:
    lines.append(line.rstrip())

width = len(lines[0])

for line in lines:
    if (line[x] == "#"):
        treecount += 1
    x += 3
    x %= width

print("We hit a stunning {} trees. 🌲".format(treecount))