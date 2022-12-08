import re

def find_calories(filename):
    calories = []
    with open(filename) as f:
        data = f.read()
        # split the data by a newline followed by one or more newlines
        # this separates the inventory of each elf
        for elf in re.split(r"\n{2,}", data):
        # split the inventory by newline and convert each line to an integer
        # then sum the list to find the total number of calories
            calories.append(sum(map(int, elf.split("\n"))))
        # return the elf carrying the most calories and the number of calories they are carrying
    return max(enumerate(calories), key=lambda x: x[1])

print(find_calories("day-1/input.txt"))