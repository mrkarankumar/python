import math

def print_heart():
    for i in range(6, -7, -1):
        for j in range(-7, 8):
            if math.sqrt(i**2 + j**2) <= 5 + i % 2:
                print('*', end='')
            else:
                print(' ', end='')
        print()

print_heart()
