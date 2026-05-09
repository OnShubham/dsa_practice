vovel = "aouel"
name = "shubam"
res = ""

for char in name:
    if char in vovel:
        res += "*"
    else:
        res += char
print(res)