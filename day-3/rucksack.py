def get_priority(letter):
    if letter >= 'A' and letter <= 'Z':
        return ord(letter) - ord('A') + 27
    else:
        return ord(letter) - ord('a') + 1

def calculate_value(line):
    values = [0] * 53
    for i in range(len(line)//2):
        values[get_priority(line[i])] = 1

    for i in range(len(line)//2, len(line)):
        if values[get_priority(line[i])] == 1:
            return get_priority(line[i])
    return 0 # toto by nealo nastat


def main():
    sum = 0
    with open("day-3/input.in", "r") as f:
        for line in f.readlines():
            sum += calculate_value(line.strip())

    print(sum)

if __name__ == "__main__":
    main()