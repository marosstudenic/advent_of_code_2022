class Simulation:
    def __init__(self, default_width_of_plain):
        self.plain_visited = [[0 for i in range(default_width_of_plain)] for x in range(default_width_of_plain)]
        self.head_position = (0,0)
        self.visted = set()
        self.tail_position = (0,0)

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
            diff_x = abs(new_head_position[0] - self.tail_position[0])
            diff_y = abs(new_head_position[1] - self.tail_position[1])
            if diff_x > 1 or diff_y > 1:
                self.tail_position = self.head_position
            self.head_position = new_head_position
            x, y = self.tail_position
            self.plain_visited[x][y] = 1
            self.visted.add(self.tail_position) 
            # self.print_visited()
            # print("----")

       
    
    def count_visited(self):
        v = set()
        print(sum([sum(x) for x in self.plain_visited]))
        for row in range(len(self.plain_visited)):
            for col in range(len(self.plain_visited[row])):
                if self.plain_visited[row][col] == 1:
                    v.add((row, col))

        print(v.difference(self.visted), len(v.difference(self.visted)))
        return len(self.visted)

    def print_visited(self):
        print("\n".join(["".join(["." if x==0 else "#" for x in y ]) for y in reversed(self.plain_visited)]))

def main():
    simulation = Simulation(400)
    with open("day-9/input.in", "r") as f:
        for line in f.readlines():
            simulation.calculate_value(line.strip())

    print(simulation.count_visited())

# 6188
if __name__ == "__main__":
    main()