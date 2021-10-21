f = open("./input.txt", "r")
lines = []
results = []
product = 1

slopes = [
    (1,1),
    (3,1),
    (5,1),
    (7,1),
    (1,2)
]

for line in f:
    lines.append(line.rstrip())

width = len(lines[0])

def simulate(a, b):
    treecount = 0
    x = 0
    for line in lines[::b]:
        if (line[x] == "#"):
            treecount += 1
        x += a
        x %= width
    return treecount

for slope in slopes:
    results.append(simulate(slope[0], slope[1]))

for result in results:
    product *= result

print("Results: {} - Product: {}".format(results, product))