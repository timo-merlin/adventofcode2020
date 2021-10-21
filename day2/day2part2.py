f = open("./input.txt", "r")
entries = []
validcount = 0

for line in f:
    entries.append(line.rstrip())

def check(entry):
    a = int(entry.split('-')[0])
    b = int(entry.split('-')[1].split(' ')[0])
    char = entry.split(' ')[1][0]
    pwd = entry.split(' ')[-1]

    if ((pwd[a-1] == char) ^ (pwd[b-1] == char)):
        return 1
    else: 
        return 0

for entry in entries:
    validcount += check(entry)

print("There are {} valid entries in the dataset.".format(validcount))