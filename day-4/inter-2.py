
def calculate_value(line):
    section1, section2 = line.split(",")
    section1 = [int(z) for z in section1.split("-")]
    section2 = [int(z) for z in section2.split("-")]
    section1 = set(range(section1[0], section1[1]+1))
    section2 = set(range(section2[0], section2[1]+1))

    return len(section1.intersection(section2)) > 0
    

def main():
    sum = 0
    with open("day-4/input.in", "r") as f:
        for line in f.readlines():
            sum += calculate_value(line.strip())

    print(sum)

if __name__ == "__main__":
    main()