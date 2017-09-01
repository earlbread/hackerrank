#!/usr/bin/env python3

def getRegionSize(grid, row, col):
    rows = len(grid)
    cols = len(grid[0])

    if row < 0 or col < 0 or row >= rows or col >= cols:
        return 0

    if grid[row][col] == 0:
        return 0

    grid[row][col] = 0

    regionSize = 1

    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if i != row or j != col:
                regionSize += getRegionSize(grid, i, j)

    return regionSize


def getBiggestRegion(grid):
    maxRegionSize = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            regionSize = getRegionSize(grid, i, j)
            maxRegionSize = max(regionSize, maxRegionSize)

    return maxRegionSize


n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
print(getBiggestRegion(grid))
