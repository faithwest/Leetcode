n = 10

def triangle(n):
    for i in range(n, 0, -1):
        print(f'{i}')
        for j in range(n - i):
            print(' ', end='')
        for j in range(2 * i - 1):
            print('*', end='')
        print()

triangle(n)

################################################################
def upside(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            print(' ', end='')
        for j in range(2 * i - 1):
            print('*', end='')
        print()

n = 5
upside(n)
