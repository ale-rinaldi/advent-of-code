with open("d4-input.txt", "r") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

passports = []
passport = {}
for line in lines:
    if line == "":
        passports.append(passport)
        passport = {}
        continue
    fields = line.split(" ")
    for field in fields:
        field_arr = field.split(':')
        key = field_arr[0]
        val = field_arr[1]
        passport[key] = val
passports.append(passport)
    
valid = 0
for passport in passports:
    if "byr" not in passport:
        continue
    byr = int(passport["byr"])
    if byr < 1920 or byr > 2002:
        continue
    if "iyr" not in passport:
        continue
    iyr = int(passport["iyr"])
    if iyr < 2010 or iyr > 2020:
        continue
    if "eyr" not in passport:
        continue
    eyr = int(passport["eyr"])
    if eyr < 2020 or eyr > 2030:
        continue
    if "hgt" not in passport:
        continue
    hgt = passport["hgt"]
    hgt_unit = hgt[-2:]
    hgt_val = int(hgt[:-2])
    if hgt_unit == "cm":
        if hgt_val < 150 or hgt_val > 193:
            continue
    elif hgt_unit == "in":
        if hgt_val < 59 or hgt_val > 76:
            continue
    else:
        continue
    if "hcl" not in passport:
        continue
    hcl = passport["hcl"]
    if len(hcl) != 7:
        continue
    if hcl[0] != "#":
        continue
    if len([character for character in list(hcl)[1:] if character not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]]) > 0:
        continue
    if "ecl" not in passport:
        continue
    ecl = passport["ecl"]
    if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        continue
    if "pid" not in passport:
        continue
    pid = passport["pid"]
    if len(pid) != 9:
        continue
    try:
        int(pid)
    except:
        continue
    valid += 1

print(valid)
