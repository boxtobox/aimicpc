import sys
from math import sqrt, ceil

N = int(sys.stdin.readline())
k = N - 1


def quadratic_eq(n):  # problem-specific function. must NOT generally use.
    a, b, c = 3, 3, -n
    return (b * (-1) + sqrt(b * b - 4 * a * c)) / (2 * a)


result = ceil(quadratic_eq(k)) + 1

print(result)
