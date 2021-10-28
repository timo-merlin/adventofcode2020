f = open("./input.txt", "r")
groups = []
solution = 0

for line in f:
    if line.rstrip() == '':
        groups.append([])
    else:
        if (len(groups) > 0):
            groups[-1].append(line.rstrip())
        else:
            groups.append([])
            groups[-1].append(line.rstrip())


for group in groups:
    key = list(group[0])
    for answer in group[1:]:
        removes = []
        for char in key:
            if char in answer:
                continue
            else:
                removes.append(char)
        for r in removes:
            key.remove(r)

    solution += len(key)

print("The solution is: {}".format(solution))