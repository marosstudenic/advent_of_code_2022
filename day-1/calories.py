def main():
    elfs = [0]
    with open("input.txt", "r") as f:
        for line in f.readlines():
            if (line == '\n'):
                elfs += [0]
            else:
                elfs[-1] += int(line.strip())

    print(sorted(elfs)[-1])

if __name__ == "__main__":
    main()
