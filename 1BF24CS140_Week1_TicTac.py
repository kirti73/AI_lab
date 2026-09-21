B = [' '] * 9

W = [
    (0,1,2), (3,4,5), (6,7,8),
    (0,3,6), (1,4,7), (2,5,8),
    (0,4,8), (2,4,6)
]

def win(p):
    return any(B[a] == B[b] == B[c] == p for a,b,c in W)

def minimax(turn):
    if win('O'):
        return 1
    if win('X'):
        return -1
    if ' ' not in B:
        return 0

    if turn == 'O':
        best = -999

        for i in range(9):
            if B[i] == ' ':
                B[i] = 'O'
                best = max(best, minimax('X'))
                B[i] = ' '       # backtrack

        return best

    else:
        best = 999

        for i in range(9):
            if B[i] == ' ':
                B[i] = 'X'
                best = min(best, minimax('O'))
                B[i] = ' '       # backtrack

        return best


def computer_move():
    best = -999
    move = -1

    for i in range(9):
        if B[i] == ' ':
            B[i] = 'O'
            score = minimax('X')
            B[i] = ' '           # backtrack

            if score > best:
                best = score
                move = i

    B[move] = 'O'


def show():
    print()
    for i in range(0, 9, 3):
        print(B[i], '|', B[i+1], '|', B[i+2])
        if i < 6:
            print('--+---+--')
    print()


print("You = X")
print("Computer = O")

while True:
    show()

    p = int(input("Enter position (1-9): ")) - 1

    if p < 0 or p > 8 or B[p] != ' ':
        print("Invalid move")
        continue

    B[p] = 'X'

    if win('X'):
        show()
        print("You win!")
        break

    if ' ' not in B:
        show()
        print("Draw!")
        break

    computer_move()

    if win('O'):
        show()
        print("Computer wins!")
        break

    if ' ' not in B:
        show()
        print("Draw!")
        break
