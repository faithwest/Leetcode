#fsctorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = 5
print(f"The factorial of {number} is {factorial(number)}")


#fibonacci
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

number = 6
print(f"The {number}th Fibonacci number is {fibonacci(number)}")

#binarry
