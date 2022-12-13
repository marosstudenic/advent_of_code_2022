from ast import literal_eval
from functools import cmp_to_key
def compare(s1, s2):
    s1 = literal_eval(s1)
    s2 = literal_eval(s2)

    result = is_greater(s1, s2)
    return result

    
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
    
    inputs += ["[[2]]"]
    inputs += ["[[6]]"]


    solver = sorted(inputs, key=cmp_to_key(compare), reverse=True)

    key1 = solver.index("[[2]]") +1
    key2 = solver.index("[[6]]") +1

    print(key1, key2)
    print(key1*key2)



if __name__ == "__main__":
    main()