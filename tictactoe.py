def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], end=" | ")
        print("\n-------------")

def check_winner(board):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]

    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != " ":
            return board[0][j]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def is_board_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print("Player", current_player, "turn")

        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        if board[row][col] != " ":
            print("Invalid move. Try again.")
            continue

        board[row][col] = current_player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print("Player", winner, "wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

play_game()
