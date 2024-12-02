col1, col2 = [], []
for line in open(0).read().splitlines():
    line = line.strip().split()
    col1.append(int(line[0]))
    col2.append(int(line[1]))

zipped = list(zip(sorted(col1), sorted(col2)))
distances = sum(abs(x[0] - x[1]) for x in zipped)
print(F"Part 1: {distances}")

similarity = 0
for e1 in col1:
   similarity += e1 * col2.count(e1)
print(f"Part 2: {similarity}")
