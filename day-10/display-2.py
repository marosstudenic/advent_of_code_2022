
   
class Simulation:
    def __init__(self):
        self.sum = 1
        self.cycle_num = 0
        self.signal_strength = 0
        self.display = [[" " for i in range(40)] for x in range(6)]
   
    def process_value(self, line):
        if line == "noop":
            yield self.sum
        else:
            yield self.sum
            yield self.sum + int(line.split()[1])

    def draw_pixel(self):
        if self.cycle_num % 40 == self.sum or self.cycle_num % 40 == self.sum + 1 or self.cycle_num % 40 == self.sum - 1:
            self.display[self.cycle_num // 40][self.cycle_num % 40 ] = "#"

    def position(self):
        return (self.cycle_num % 40, self.cycle_num // 40)

    def print_signal_strength(self):
        print(self.signal_strength)

    def print_display(self):
        print("\n".join(["".join(y) for y in self.display]))

def main():
    simulation = Simulation()
    with open("day-10/input.in", "r") as f:
        for line in f.readlines():
            for state in simulation.process_value(line.strip()):
                simulation.draw_pixel()
                simulation.cycle_num += 1
                simulation.sum = state
                

                
        simulation.print_display()               
if __name__ == "__main__":
    main()