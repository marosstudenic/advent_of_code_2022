def move(columns, line):
    words = line.split()
    count = int(words[1]) 
    from_i = int(words[3]) -1
    to_i = int(words[5]) -1

    columns[to_i] += columns[from_i][-count:]
    columns[from_i] = columns[from_i][:-count]
    

def main():
    sum = 0
    with open("day-5/input.in", "r") as f:
        inputs = [line[:-1] for line in f.readlines()]
    inde = 0
    loading_crates = True
    count_of_columns = len(inputs[0])//4 +1 # each column is 4 char wide except last one

    columns = [[] for i in range(count_of_columns)]
    # parsing columns
    while True:
        if inputs[inde] == '':
            loading_crates = False

        if loading_crates:
            for i in range(count_of_columns):
                if inputs[inde][4*i +1] != ' ' and not(inputs[inde][4*i+1].isnumeric()):
                    columns[i] += [inputs[inde][4*i+1]]

        else:
            print(columns)
            inde+=1
            break
        inde+=1


    for column in columns:
        column.reverse()

    print(columns)
    for ind in range(inde, len(inputs)):
        move(columns, inputs[ind])
    print(columns)

    for i in range(count_of_columns):
        print(columns[i][-1], end="")
    print()
    
    



if __name__ == "__main__":
    main()