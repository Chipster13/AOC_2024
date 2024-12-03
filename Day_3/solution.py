import regex as re

data = open(0).read()
results = 0
groups = re.findall(r'mul\((-?\d{1,3}),(-?\d{1,3})\)', data)
for group in groups:
    results += int(group[0]) * int(group[1])
print(f"Part 1: {results}")

results = 0
ignore = False
groups = re.findall(r"mul\((-?\d{1,3}),(-?\d{1,3})\)|(don't\(\))|(do\(\))", data)
for group in groups:
    if group[2] == "don't()":
        ignore = True
    elif group[3] == 'do()':
        ignore = False
    else:
        if not ignore:
            results += int(group[0]) * int(group[1])

print(f"Part 2: {results}")