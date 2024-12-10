from collections import deque

def calculate_routes(row: int, col: int) -> tuple[int, int]:
    q = deque([(row, col)])
    nines = set()
    counts = 0
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q:
        r, c = q.popleft()
        for dr, dc in dirs:
            nr = r+dr
            nc = c+dc
            if not(0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == grid[r][c] + 1):
                continue
            if grid[nr][nc] == 9:
                nines.add((nr, nc))
                counts += 1
                continue
            else:
                q.append((nr, nc))

    return len(nines), counts

grid = [list(map(int, line.strip())) for line in open(0).readlines()]
zeros = [(r, c) for r, row in enumerate(grid) for c, val in enumerate(row) if val == 0]
total = 0
routes = 0
for r, c in zeros:
    l, counts = calculate_routes(r, c)
    total += l
    routes += counts
print(f"Part 1: {total}")
print(f"Part 2: {routes}")
