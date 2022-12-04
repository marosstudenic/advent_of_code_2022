
def calculate_value(line):
    section1, section2 = line.split(",")
    section1 = [int(z) for z in section1.split("-")]
    section2 = [int(z) for z in section2.split("-")]
    section1.sort()
    section2.sort()
    return \
    (section1[0] >= section2[0] and section1[1] <= section2[1]) \
    or (section2[0] >= section1[0] and section2[1] <= section1[1]) \
    or (section1[0] >= section2[0] and section1[0] <= section2[1]) \
    or (section1[1] >= section2[0] and section1[1] <= section2[1]) 

def main():
    sum = 0
    with open("day-4/input.in", "r") as f:
        for line in f.readlines():
            if not(calculate_value(line.strip())):
                print(line)
            else:
                sum += 1

    print(sum)

if __name__ == "__main__":
    main()