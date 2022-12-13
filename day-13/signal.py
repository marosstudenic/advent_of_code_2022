from ast import literal_eval
def compare(s1, s2):
    s1 = literal_eval(s1)
    s2 = literal_eval(s2)

    result = is_greater(s1, s2)
    if abs(result):
        if result == -1:
            print("smaller")
            print(s1, s2)
            return False
        else:
            print("greater")
            print(s1, s2)
            return True
    else:
        print("equal")
        print(s1, s2)
        raise(Exception("equal"))

    
def is_greater(s1, s2):
    if len(s1) == 0 and len(s2) > 0:
        return 1
    for i in range(len(s1)):
        # last item in second list, but not in first list
        if i >= len(s2):
            return -1
        if type(s1[i]) == list and type(s2[i]) == list:
            result = is_greater(s1[i], s2[i])
            if abs(result):
                return result
            else:
                if i == len(s1) - 1 and i < len(s2) - 1:
                    return 1
                else:
                    continue
            
        elif type(s1[i]) == list and type(s2[i]) != list:
            result = is_greater(s1[i], [s2[i]])
            if abs(result):
                return result
            else:
                if i == len(s1) - 1 and i < len(s2) - 1:
                    return 1
                else:
                    continue

        
        elif type(s1[i]) != list and type(s2[i]) == list:
            result = is_greater([s1[i]], s2[i])
            if abs(result):
                return result
            else:
                if i == len(s1) - 1 and i < len(s2) - 1:
                    return 1
                else:
                    continue
    
        if s1[i] > s2[i]:
            return -1

        if s1[i] < s2[i]:
            return 1

        # last item in first list, but not in second list
        if i == len(s1) - 1 and i < len(s2) - 1:
            return 1
    return 0
    


def main():
    sum = 0
    with open("day-13/input.in", "r") as f:
        inputs = f.read().splitlines(keepends=False)
        inputs = list(filter(lambda x: x != "", inputs))
    
    for indice in range(len(inputs)//2):
        if compare(inputs[indice*2], inputs[indice*2+1]):
            # print(inputs[indice*2], inputs[indice*2+1])
            # print("Yes")
            sum+= indice +1
        # else:
        #     print(inputs[indice*2], inputs[indice*2+1])
        #     print("No")

    print(sum)

if __name__ == "__main__":
    main()