# create bfs algoithm, which takes a grid of letters, and you can move in any direction by one, and you can only move to a letter that is greater than the current letter by one (a->b, b->c, etc), or you can move to letter that is less than current letter. The goal is to find the shortest Path  in the grid, and return the length of the path.
# start is at S, end is at E
# start has alleviation of a, end has alleviation of z

# example input:
# Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi

# example output:
# 31

x = 0
y = 0
grid = []
with open("day-12/input.in", "r") as f:
    for line in f:
        grid.append(list(line.strip()))
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                x = i
                y = j
                break
    
    print(x, y)
    print(grid)


def diff(a, b):
    if (a == "E"):
        a = "z"
    if (b == "S"):
        b = "a"
    return ord(a) - ord(b)


def bfs(grid, x, y):
    queue = [(x, y, 0)]
    visited = set()
    while queue:
        x, y, dist = queue.pop(0)
        if grid[x][y] == "E":
            return dist
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and diff(grid[x+dx][y+dy], grid[x][y]) <= 1 and (x + dx, y + dy) not in visited:
                queue.append((x + dx, y + dy, dist + 1))
    return -1

print(bfs(grid, x, y))
