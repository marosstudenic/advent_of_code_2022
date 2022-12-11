class Monkey:
    def __init__(self, list):
        self.items = [int(x) for x in list[1].split(":")[1].split(", ")]
        self.operator = list[2].split()[4]
        self.operand = list[2].split()[5]
        self.test = int(list[3].split()[3])
        self.test_true = int(list[4].split()[5])
        self.test_false = int(list[5].split()[5])
        self.inspection_count = 0

    def inspect_items(self):
        self.inspection_count += len(self.items)
        for item in self.items:
            inspection_value = self.do_operation(item) //3
            if inspection_value % self.test == 0:
                yield self.test_true, inspection_value
            else:
                yield self.test_false, inspection_value
        self.items = []

    def do_operation(self, item):
        if self.operand == "old":
            operand = item
        else:
            operand = int(self.operand)

        if self.operator == "*":
            return item * operand
        elif self.operator == "+":
            return item + operand
        elif self.operator == "-":
            return item - operand
        elif self.operator == "/":
            return item / operand
        else:
            print("Unknown operator: ", self.operator)
            return None




def main():
    with open("day-11/input.in", "r") as f:
        inputs = list(map(lambda line: line.strip(), f.read().splitlines(keepends=False)))

    monkeys = []
    for mokey in range(len(inputs)//7 + 1):
        monkeys.append(Monkey(inputs[mokey*7:mokey*7+6]))

    for round in range(20):
        for monkey in monkeys:
            for monkey_index, item in monkey.inspect_items():
                monkeys[monkey_index].items.append(item)
    values = []
    for monkey in monkeys:
        values.append(monkey.inspection_count)

    values.sort(reverse=True)
    print(values)
    print(values[0]* values[1])

    


if __name__ == "__main__":
    main()