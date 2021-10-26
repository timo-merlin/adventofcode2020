import re
f = open("./input.txt", "r")
passports = []
lastline = ' '
validcount = 0

def byr(p):
    if ('byr' not in p):
        return False
    val = p['byr']
    if (len(val) == 4) and (1920 <= int(val) <= 2002):
        return True
    return False

def iyr(p):
    if ('iyr' not in p):
        return False
    val = p['iyr']
    if (len(val) == 4) and (2010 <= int(val) <= 2020):
        return True
    return False

def eyr(p):
    if ('eyr' not in p):
        return False
    val = p['eyr']
    if (len(val) == 4) and (2020 <= int(val) <= 2030):
        return True
    return False

def hgt(p):
    if ('hgt' not in p):
        return False
    unit = p['hgt'][-2:]
    val = p['hgt'][:-2]
    if (unit == "cm") and (150 <= int(val) <= 193):
        return True
    elif (unit == "in") and (59 <= int(val) <= 76):
        return True
    return False

def hcl(p):
    if ('hcl' not in p):
        return False
    val = p['hcl']
    if bool(re.fullmatch(r"#[0-9a-f]{6}", val)):
        return True
    return False

def ecl(p):
    if ('ecl' not in p):
        return False
    val = p['ecl']
    if bool(re.fullmatch(r"((amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)){1}", val)):
        return True
    return False

def pid(p):
    if ('pid' not in p):
        return False
    val = p['pid']
    if bool(re.fullmatch(r"[0-9]{9}", val)):
        return True
    return False

for line in f:
    if (lastline.isspace()):
        passports.append(line.rstrip())
    else:
        passports[-1] += ' ' + line.rstrip()
    lastline = line 

for passport in passports:
    passport = passport.split()

    fields = {}

    for pair in passport:
        fields[pair.split(':')[0]] = pair.split(':')[1]


    # if (all( byr(passport), iyr(passport), eyr(passport), hgt(passport), hcl(passport), ecl(passport), pid(passport) )):
    #     validcount += 1

    if ( all( [byr(fields), iyr(fields), eyr(fields), hgt(fields), hcl(fields), ecl(fields), pid(fields)] )):
        validcount += 1


print("The amount of valid passports is {}.".format(validcount))