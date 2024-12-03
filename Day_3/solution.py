import regex as re

data = open(0).read()
part1 = 0
part2 = 0
ignore = False
groups = re.findall(r"mul\((-?\d{1,3}),(-?\d{1,3})\)|(don't\(\))|(do\(\))", data)
for group in groups:
    if "don't()" in group:
        ignore = True
    elif "do()" in group:
        ignore = False
    else:
        part1 += int(group[0]) * int(group[1])
        if not ignore:
            part2 += int(group[0]) * int(group[1])

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
