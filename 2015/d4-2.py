import hashlib

input = "iwrupvqb"

x = 0
while True:
    to_encode = f"{input}{x}"
    md5 = hashlib.md5(to_encode.encode('utf-8')).hexdigest()
    if md5[:6] == "000000":
        print(x)
        break
    x += 1