def display(board):
    print()
    print(" | ".join(board[:3]))
    print("--+---+--")
    print(" | ".join(board[3:6]))
    print("--+---+--")
    print(" | ".join(board[6:]))
    print()


def win(board, p):
    w = [(0,1,2),(3,4,5),(6,7,8),
         (0,3,6),(1,4,7),(2,5,8),
         (0,4,8),(2,4,6)]

    return any(board[a] == board[b] == board[c] == p for a,b,c in w)


def minimax(board, max_player):
    if win(board, "O"):
        return 1
    if win(board, "X"):
        return -1
    if " " not in board:
        return 0

    scores = []

    for i in range(9):
        if board[i] == " ":
            board[i] = "O" if max_player else "X"
            scores.append(minimax(board, not max_player))
            board[i] = " "

    return max(scores) if max_player else min(scores)


def computer_move(board):
    best = -1000
    move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "

            if score > best:
                best = score
                move = i

    return move


print("TIC TAC TOE")
print("You are X")
print("Computer is O")

board = [" "] * 9
display(board)

while True:

    while True:
        pos = int(input("Enter position (1-9): "))

        if 1 <= pos <= 9 and board[pos-1] == " ":
            break

        print("Invalid or occupied position!")

    board[pos-1] = "X"
    display(board)

    if win(board, "X"):
        print("You win!")
        break

    if " " not in board:
        print("Game is a Draw!")
        break

    move = computer_move(board)
    board[move] = "O"

    print("Computer chose:", move + 1)
    display(board)

    if win(board, "O"):
        print("Computer wins!")
        break

    if " " not in board:
        print("Game is a Draw!")
        break
