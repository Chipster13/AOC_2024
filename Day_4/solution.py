grid = open(0).read().splitlines()
count = 0
dirs = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 'X':
            for dr, dc in dirs:
                if not (0 <= r + 3*dr < len(grid) and 0 <= c + 3*dc < len(grid[0])):
                    continue
                if grid[r + dr][c + dc] == 'M' and grid[r + 2 * dr][c + 2 * dc] == 'A' and grid[r + 3 * dr][c + 3 * dc] == 'S':
                    count += 1

print(f"Part 1: {count}")

#M.S
#.A.
#M.S
# Letters around the A are in a pattern: MSSM, SSMM, SMMS, MMSS
#
count = 0
for r in range(1, len(grid)-1):         # 'A' can't be on an edge
    for c in range(1, len(grid[0])-1):  # ditto
        if grid[r][c] == 'A':
            corners = [grid[r-1][c-1], grid[r-1][c+1], grid[r+1][c+1], grid[r+1][c-1]]
            if ''.join(corners) in ['MSSM', 'SSMM', 'SMMS', 'MMSS']:
                count += 1

print(f"Part 2: {count}")