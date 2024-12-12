# Credit to HyperNeutrino for this cache fuction from functools
# and learning about the @ decorator

from functools import cache

@cache
def calc_stones(stone, n):
    if n == 0:
        return 1
    if stone == 0:
        return calc_stones(1, n-1)
    if  len(str(stone)) % 2 == 0:
        s = str(stone)
        l = len(s) // 2
        return calc_stones(int(s[:l]), n-1) + calc_stones(int(s[l:]), n-1)
    else:
        return calc_stones(stone * 2024, n-1)

data = [int(x) for x in open('in.txt').read().split()]
print(f"Part 1: {sum(calc_stones(stone, 25) for stone in data)}")
print(f"Part 2: {sum(calc_stones(stone, 75) for stone in data)}")
