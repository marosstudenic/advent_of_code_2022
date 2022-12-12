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

start = (0, 0)
end = (0, 0)
grid = []
list_a = []
with open("day-12/input.in", "r") as f:
    for line in f:
        grid.append(list(line.strip()))
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                start = (i, j)
                grid[i][j] = "a"
            elif grid[i][j] == "E":
                end = (i, j)
                grid[i][j] = "z"
            elif grid[i][j] == "a":
                list_a.append((i, j))
    

def diff(a, b):
    return ord(a) - ord(b)


def bfs(grid, start):
    queue = [(start[0], start[1], 0)]
    visited = set()
    while queue:
        x, y, dist = queue.pop(0)
        if (x, y) == end:
            return dist
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and diff(grid[x+dx][y+dy], grid[x][y]) <= 1 and (x + dx, y + dy) not in visited:
                queue.append((x + dx, y + dy, dist + 1))
    return float("inf")

def part_one():
    print(bfs(grid, start))

def part_two():
    print(min(bfs(grid, a) for a in list_a))

part_one()
part_two()