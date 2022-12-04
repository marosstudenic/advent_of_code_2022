def get_priority(letter):
    if letter >= 'A' and letter <= 'Z':
        return ord(letter) - ord('A') + 27
    else:
        return ord(letter) - ord('a') + 1

def calculate_value(line1, line2, line3):
    values = [0] * 53
    for i in range(len(line1)):
        values[get_priority(line1[i])] = 1

    for i in range(len(line2)):
        if values[get_priority(line2[i])] == 1:
            values[get_priority(line2[i])] = 2

    for i in range(len(line3)):
        if values[get_priority(line3[i])] == 2:
            return get_priority(line3[i])
    return 0 # toto by nealo nastat


def main():
    sum = 0
    with open("day-3/input.in", "r") as f:
        lines = []
        for line in f.readlines():
            lines.append(line.strip())
            if len(lines) == 3:
                sum += calculate_value(lines[0], lines[1], lines[2])
                lines = []
    print(sum)

if __name__ == "__main__":
    main()