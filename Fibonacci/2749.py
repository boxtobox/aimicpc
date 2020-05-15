from sys import stdin
from math import log2, floor

mod = 10 ** 6
# MAX:  1000000000000000000


def dec_to_bin(n):
    a = []
    while True:
        v, n = n % 2, n // 2
        a.append(v)
        if n < 1:
            break
    return a


def matrix_doubles(k):
    m = [((1, 1), (1, 0))]
    for i in range(1, k):
        m.append(matrix_multiply(m[-1], m[-1]))
    return m


def matrix_multiply(matA, matB):
    (a, b), (c, d) = matA
    (e, f), (g, h) = matB
    return [[(a*e + b*g) % mod, (a*f + b*h) % mod], [(c*e + d*g) % mod, (c*f + d*h) % mod]]


N = int(stdin.readline())
if N == 0:
    print(0)
elif N == 1:
    print(1)
else:
    size = floor(log2(N-1)) + 1
    matrix_bin = dec_to_bin(N-1)
    matrix_double = matrix_doubles(size)
    result = [[1, 0], [0, 1]]  # identity matrix
    for k in range(size):
        if matrix_bin[k]:
            result = matrix_multiply(result, matrix_double[k])
    print(result[0][0] % mod)
