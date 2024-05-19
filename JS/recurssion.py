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
def binary_search(arr, low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, low, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, high, target)

arr = [2, 3, 4, 10, 40]
target = 10
result = binary_search(arr, 0, len(arr) - 1, target)
if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
