def is_safe(r):
    diffs = [x - y for x, y in zip(r, r[1:])]
    return all(1 <= x <= 3 for x in diffs) or all(-1 >= x >= -3 for x in diffs)

data = open(0).readlines()
safe = 0
for line in data:
    report = list(map(int, line.split()))
    if is_safe(report):
        safe += 1

print(f"Part 1: {safe}")

safe = 0
for line in data:
    report = list(map(int, line.split()))
    if any(is_safe(report[:i] + report[i + 1:]) for i in range(len(report))):
        safe += 1

print(f"Part 2: {safe}")
