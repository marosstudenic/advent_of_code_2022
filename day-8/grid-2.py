
def count_distance(grid, row, column, direction):
    height = grid[row][column]
    distance = 0
    row+=direction[0]
    column+=direction[1]
    len_grid = len(grid)
    while row < len_grid and column < len_grid and row >= 0 and column >= 0:
        distance += 1
        if grid[row][column] >= height:
            return distance
        row += direction[0]
        column += direction[1]
    return distance

def count_scentic_score(grid, row, column):
    score = 1
    for direction in [[-1,0],[1,0],[0,-1],[0,1]]:
        distance = count_distance(grid, row, column, direction)
        if distance == 0:
            return 0
        score *= distance
    return score




def calculate_value(inputs):
    blocks_count = [[0 for x in range(len(inputs))] for i in range(len(inputs))]

    grid = [[0 for x in range(len(inputs))] for i in range(len(inputs))]
    for i in range(len(inputs)):
        for j in range(len(inputs)):
            grid[i][j] = int(inputs[i][j])


    print('\n'.join([str(line) for line in grid]))

    # for top-down 
    max_scentic = 0
    for column in range(len(inputs)):
        for row in range(len(inputs)):
            new = count_scentic_score(grid, row, column)
            if max_scentic < new:
                max_scentic = new
                position = (row, column)

    print(position)
    return max_scentic


def main():
    with open("day-8/input.in", "r") as f:
        inputs = [ line.strip() for line in f.readlines()]

    print(calculate_value(inputs))

if __name__ == "__main__":
    main()