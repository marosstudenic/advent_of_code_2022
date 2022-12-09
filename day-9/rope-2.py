class Simulation:
    def __init__(self, knots_count):
        self.head_position = (0,0)
        self.visted = set()
        self.knots_count = knots_count
        self.knots_positions = [(0,0) for i in range(self.knots_count)]
        self.moves_rules = {
            (2, 1) : (1, 1),
            (1, 2) : (1, 1),
            (1, 1) : (0, 0),
            (0, 0) : (0, 0),
            (2, 0) : (1, 0),
            (0, 2) : (0, 1),
            (2,2) : (1, 1),
            (-2, 1) : (-1, 1),
            (-1, 2) : (-1, 1),
            (-2, 0) : (-1, 0),
            (0, -2) : (0, -1),
            (-2, -2) : (-1, -1),
            (-2, -1) : (-1, -1),
            (-1, -2) : (-1, -1),
            (1, -2) : (1, -1),
            (2, -2) : (1, -1),
            (2, -1) : (1, -1),
            (-2, 2) : (-1, 1),
        }

    def calculate_value(self, line):
        direction, value = line.split()
        value = int(value)
    
        if direction == "L":
            self.move((-1, 0), value)
            
        elif direction == "R":
            self.move((1, 0), value)

        elif direction == "U":
            self.move(( 0, 1), value)

        elif direction == "D":
            self.move(( 0, -1), value)
        else:
            raise Exception("Invalid direction")
    
    def move(self, direction, value):
        for i in range(value):
            new_head_position = (self.head_position[0] + direction[0], self.head_position[1] + direction[1])
            if self.should_move(new_head_position, self.knots_positions[0]):
                self.knots_positions[0] = self.head_position

                for i in range(1, len(self.knots_positions)):
                    if self.should_move( self.knots_positions[i-1], self.knots_positions[i]):
                        move = self.detect_move(self.knots_positions[i-1], self.knots_positions[i])
                        self.knots_positions[i] = (self.knots_positions[i][0] + move[0], self.knots_positions[i][1] + move[1])
                    else:
                        break    
            self.head_position = new_head_position
            self.visted.add(self.knots_positions[self.knots_count-1]) 

    def should_move(self, curr, tail):
            diff_x = abs(curr[0] - tail[0])
            diff_y = abs(curr[1] - tail[1])
            if diff_x > 1 or diff_y > 1:
                return True
            else:
                return False

    def detect_move(self, curr, tail):
        diff_x = curr[0] - tail[0]
        diff_y = curr[1] - tail[1]
        return self.moves_rules[(diff_x, diff_y)]

    def count_visited(self):
        self.print_visited()
        return len(self.visted)

    def print_visited(self):
        max_x = max([x for x, y in self.visted])
        max_y = max([y for x, y in self.visted])
        min_x = min([x for x, y in self.visted])
        min_y = min([y for x, y in self.visted])

        plain_visited = [[0 for i in range(max_y - min_y + 1)] for j in range(max_x - min_x + 1)]
        for x, y in self.visted:
            plain_visited[x - min_x][y - min_y] = 1
        
        for row in range(len(plain_visited)-1, -1, -1):
            for cell in range(len(plain_visited[row])):
                if plain_visited[row][cell] == 0:
                    print(".", end="")
                else:
                    print("#", end="")
            print()

def main():
    simulation = Simulation(9)
    with open("day-9/input.in", "r") as f:
        for line in f.readlines():
            simulation.calculate_value(line.strip())

    print(simulation.count_visited())

# 6188
if __name__ == "__main__":
    main()