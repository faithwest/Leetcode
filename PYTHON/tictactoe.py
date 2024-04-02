def print_board(board):
    """Prints the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    """Checks if there is a winner."""
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]  # Winner found in row
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]  # Winner found in column

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]  # Winner found in diagonal (top-left to bottom-right)
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]  # Winner found in diagonal (top-right to bottom-left)

    return None  # No winner found


def is_board_full(board):
    """Checks if the board is full."""
    for row in board:
        if " " in row:
            return False
    return True


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        row = int(input(f"Player {player}, enter row (0, 1, or 2): "))
        col = int(input(f"Player {player}, enter column (0, 1, or 2): "))

        if board[row][col] == " ":
            board[row][col] = player
        else:
            print("That position is already taken. Try again.")
            continue

        print_board(board)

        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins!")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    main()
