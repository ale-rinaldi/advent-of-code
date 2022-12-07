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
    keys = passport.keys()
    if 'byr' in keys and 'iyr' in keys and 'eyr' in keys and 'hgt' in keys and 'hcl' in keys and 'ecl' in keys and 'pid' in keys:
        valid +=1

print(valid)
