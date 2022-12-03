winning = {
    'A': 2,
    'B': 3,
    'C': 1
}

losing = {
    'A': 3,
    'B': 1,
    'C': 2
}


win_state = {
    'Y': 3,
    'Z': 6,
    'X': 0
}


def calculate_score(player1 :str):
    return ord(player1) - ord('A') + 1

def main():
    # choose, win
    score = [0, 0]
    with open("day-2/input.in", "r") as f:
        for line in f.readlines():
            player1, state =  line.strip().split()
            if state == 'X':
                score[0] += losing[player1]
            elif state == 'Z':
                score[0] += winning[player1]
            else:
                score[0] += calculate_score(player1)
            score[1]+= win_state[state]

    print(score)
    print(sum(score))

if __name__ == "__main__":
    main()
