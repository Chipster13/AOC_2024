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

def check_for_loop(part2 = False):
    r, c = find_start(grid)
    dr, dc = -1, 0
    visited = set()
    while True:
        if part2:
            if (r, c, dr, dc) in visited:
                return True
            visited.add((r, c, dr, dc))
        else:
            visited.add((r, c))
        if not(0 <= r + dr < R and 0 <= c + dc < C):
            if part2:
                return False
            else:
                return visited
        if grid[r+dr][c+dc] == '#':
            dc, dr = -dr, dc
        else:
            r += dr
            c += dc

visited = check_for_loop(False)
print(f"Part 1: {len(visited)}")

count = 0
for ro in range(R):
    for co in range(C):
        if grid[ro][co] == '.':
            grid[ro][co] = '#'
            if check_for_loop(True):
                count += 1
            grid[ro][co] = '.'

print(f"Part 2: {count}")
