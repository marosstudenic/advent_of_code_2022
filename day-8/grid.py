
def calculate_value(inputs):
    blocks_count = [[0 for x in range(len(inputs))] for i in range(len(inputs))]

    grid = [[0 for x in range(len(inputs))] for i in range(len(inputs))]
    for i in range(len(inputs)):
        for j in range(len(inputs)):
            grid[i][j] = int(inputs[i][j])


    print('\n'.join([str(line) for line in grid]))

    # for top-down 
    for column in range(len(inputs)):
        line_max = -1
        for row in range(len(inputs)):
            if grid[row][column] > line_max:
                line_max = grid[row][column]
            else:
                blocks_count[row][column] += 1

    # for bottom-up
    for column in range(len(inputs)):
        line_max = -1
        for row in range(1,len(inputs)+1):
            if grid[-row][column] > line_max:
                line_max = grid[-row][column]
            else:
                blocks_count[-row][column] += 1

    # for right-left
    for row in range(len(inputs)):
        line_max = -1
        for column in range(1,len(inputs)+1):
            if grid[row][-column] > line_max:
                line_max = grid[row][-column]
            else:
                blocks_count[row][-column] += 1
    
    # for left-right
    for row in range(len(inputs)):
        line_max = -1
        for column in range(len(inputs)):
            if grid[row][column] > line_max:
                line_max = grid[row][column]
            else:
                blocks_count[row][column] += 1


    suma = 0
    for column in range(len(inputs)):
        for row in range(len(inputs)):
            if blocks_count[row][column] < 4:
                suma +=1

    return(suma)



def main():
    with open("day-8/input.in", "r") as f:
        inputs = [ line.strip() for line in f.readlines()]

    print(calculate_value(inputs))

if __name__ == "__main__":
    main()