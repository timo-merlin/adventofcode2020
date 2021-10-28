f = open("./input.txt", "r")
lines = []
solution = 0

for line in f:
    if line.rstrip() == '':
        lines.append(line.rstrip())
    else:
        if (len(lines) > 0):
            lines[-1] += line.rstrip()
        else:
            lines.append(line.rstrip())


for line in lines:
    solution += len(set(line))

print("The solution is: {}".format(solution))