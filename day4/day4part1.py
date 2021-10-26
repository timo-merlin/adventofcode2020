f = open("./input.txt", "r")
passports = []
lastline = ' '
validcount = 0
mandatory = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

for line in f:
    if (lastline.isspace()):
        passports.append(line.rstrip())
    else:
        passports[-1] += ' ' + line.rstrip()
    lastline = line 

for passport in passports:
    passport = passport.split()

    fields = []

    for pair in passport:
        fields.append(pair.split(':')[0])

    valid = True
    for key in mandatory:
        if not (key in fields):
            valid = False
            break

    if (valid):
        validcount += 1

print("The amount of valid passports is {}.".format(validcount))