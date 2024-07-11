def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0

    while True:
        print_board(board)
        player_symbol = players[current_player]
        print(f"Player {player_symbol}'s turn.")
        row = int(input("Enter row (0, 1, 2): "))
        col = int(input("Enter column (0, 1, 2): "))

        if board[row][col] == " ":
            board[row][col] = player_symbol
            if check_winner(board, player_symbol):
                print_board(board)
                print(f"Player {player_symbol} wins!")
                break
            elif all(all(cell != " " for cell in row) for row in board):
                print_board(board)
                print("It's a tie!")
                break
            current_player = 1 - current_player
        else:
            print("That position is already taken. Try again.")

if __name__ == "__main__":
    tic_tac_toe()
