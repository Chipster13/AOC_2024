def find_start(g:[list[str]]) -> tuple[int, int]:
    for r, row in enumerate(g):
        for c, ch in enumerate(row):
            if ch == '^':
                return r, c
    return -1, -1

grid = list(map(list, open(0).read().splitlines()))
r, c = find_start(grid)
if (r, c) == (-1, -1):
    print('Unable to find start')
    exit(0)
R = len(grid)
C = len(grid[0])
dr, dc = -1, 0
visited = set()
while True:
    visited.add((r, c))
    if not (0 <= r + dr < R and 0 <= c + dc < C):
        break
    if grid[r + dr][c + dc] == '#':
        dc, dr = -dr, dc
    else:
        r += dr
        c += dc


def check_for_loop() -> bool:
    r, c = find_start(grid)
    dr, dc = -1, 0
    visited = set()
    while True:
        if (r, c, dr, dc) in visited:
            return True
        visited.add((r, c, dr, dc))
        if not(0 <= r + dr < R and 0 <= c + dc < C):
            return False
        if grid[r+dr][c+dc] == '#':
            dc, dr = -dr, dc
        else:
            r += dr
            c += dc

check_for_loop()
print(f"Part 1: {len(visited)}")

count = 0
for ro in range(R):
    for co in range(C):
        if grid[ro][co] == '.':
            grid[ro][co] = '#'
            if check_for_loop():
                count += 1
            grid[ro][co] = '.'

print(f"Part 2: {count}")
