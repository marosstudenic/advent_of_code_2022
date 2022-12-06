
def calculate_value(line):
    distinct_value = 4
    distinct = {}
    for i in range(distinct_value):
        distinct[line[i]] = distinct.get(line[i], 0) + 1
    index = distinct_value
    while index < len(line):
        distinct[line[index]] = distinct.get(line[index], 0) + 1
        distinct[line[index-distinct_value]] -= 1
        if distinct[line[index-distinct_value]] == 0:
            del distinct[line[index-distinct_value]]
        index += 1
        if len(distinct) == distinct_value:
            return index
            
    

def main():
    with open("day-6/input.in", "r") as f:
        for line in f.readlines():
            print(calculate_value(line.strip()))

if __name__ == "__main__":
    main()