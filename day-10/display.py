
   
class Simulation:
    def __init__(self):
        self.sum = 1
        self.cycle_num = 0
        self.signal_strength = 0
   
    def process_value(self, line):
        if line == "noop":
            yield (self.sum, self.cycle_num + 1)

        else:
            yield (self.sum, self.cycle_num + 1)
            yield (self.sum + int(line.split()[1]), self.cycle_num + 1)

    def detect_cycle(self):
        tmp = self.cycle_num +20
        if tmp % 40 == 38 or tmp %40 == 39:
            self.last_value = self.sum

        if tmp % 40 == 0:
            self.signal_strength += self.cycle_num * self.last_value

    def print_signal_strength(self):
        print(self.signal_strength)

def main():
    simulation = Simulation()
    with open("day-10/input.in", "r") as f:
        for line in f.readlines():
            for state in simulation.process_value(line.strip()):
                simulation.sum = state[0]
                simulation.cycle_num = state[1]
                simulation.detect_cycle()
                
        simulation.print_signal_strength()                  
if __name__ == "__main__":
    main()