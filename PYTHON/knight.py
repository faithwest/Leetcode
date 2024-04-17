def knight_moves(x, y):
    moves = [(-2, -1), (-1, -2), (1, -2), (2, -1),
             (2, 1), (1, 2), (-1, 2), (-2, 1)]
    possible_moves = []
    for dx, dy in moves:
        new_x = x + dx
        new_y = y + dy
        if 0 <= new_x < 8 and 0 <= new_y < 8:
            possible_moves.append((new_x, new_y))
    return possible_moves

# Example usage:
current_position = (3, 3)  # Knight's position on the chessboard
possible_moves = knight_moves(*current_position)
print("Possible moves from", current_position, "are:", possible_moves)
