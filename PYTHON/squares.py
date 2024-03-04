def calculate_squares(limit):
    squares = [i**2 for i in range(1, limit+1)]
    return squares

limit = int(input("Enter the limit: "))
squares_list = calculate_squares(limit)
print("Squares of numbers from 1 to", limit, "are:", squares_list)
