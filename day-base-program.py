
def calculate_value(line):
    return 0

def main():
    sum = 0
    with open("day-3/sample.in", "r") as f:
        for line in f.readlines():
            sum += calculate_value(line.strip())

    print(sum)

if __name__ == "__main__":
    main()