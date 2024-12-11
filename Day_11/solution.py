def calc_stones(stones, n):
    for _ in range(n):
        newstones = []
        for stone in stones:
            if stone == 0:
                newstones.append(1)
            elif len(str(stone)) % 2 == 0:
                s = str(stone)
                l = len(s) // 2
                newstones.append(int(s[:l]))
                newstones.append(int(s[l:]))
            else:
                newstones.append(stone * 2024)

        stones = newstones
    return len(stones)

data = [int(x) for x in open(0).read().strip().split()]
print(f"Part 1: {calc_stones(data, 25)}")
#print(f"Part 2: {calc_stones(data, 75)}")