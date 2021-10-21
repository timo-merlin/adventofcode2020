f = open("./input.txt", "r")
entries = []
validcount = 0

for line in f:
    entries.append(line.rstrip())

def check(entry):
    min = int(entry.split('-')[0])
    max = int(entry.split('-')[1].split(' ')[0])
    char = entry.split(' ')[1][0]
    pwd = entry.split(' ')[-1]

    if (min <= pwd.count(char) <= max):
        return 1
    else: 
        return 0

for entry in entries:
    validcount += check(entry)

print("There are {} valid entries in the dataset.".format(validcount))