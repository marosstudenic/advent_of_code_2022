def calculate_winner(player1, player2):
    player1 = ord(player1) - ord('A') +1
    player2 = ord(player2) - ord('X') + 1

    if player1 == player2:
        return 3
    
    if winning[str(player2)] == player1:
        return 6
    else:
        return 0 

winning = {
    '2': 1,
    '1': 3,
    '3': 2
}

def choose_score(player1 :str):
    return ord(player1) - ord('X') + 1

def main():
    # choose, win
    score = [0, 0]
    with open("day-2/input.in", "r") as f:
        for line in f.readlines():
            player1, player2 =  line.strip().split()
            score[0]+= choose_score(player2)
            score[1]+= calculate_winner(player1, player2)

    print(score)
    print(sum(score))

if __name__ == "__main__":
    main()
