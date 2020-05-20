from sys import stdin


def mat_mult(matA, matB, mod):
    (a, b), (c, d) = matA
    (e, f), (g, h) = matB
    if mod:
        return [((a * e + b * g) % mod, (a * f + b * h) % mod), ((c * e + d * g) % mod, (c * f + d * h) % mod)]
    else:
        return [(a * e + b * g, a * f + b * h), (c * e + d * g, c * f + d * h)]


def main(n):
    fib_init = [0, 1]
    if n in fib_init:
        return fib_init[n]

    n = n - 1
    result = [(1, 0), (0, 1)]  # identity matrix
    fib_pow = [(1, 1), (1, 0)]

    while True:
        v, n = n % 2, n // 2
        if v == 1:
            result = mat_mult(result, fib_pow, modulo)
        if n < 1:
            break
        fib_pow = mat_mult(fib_pow, fib_pow, modulo)
    return result[0][0]


nth = int(stdin.readline())
modulo = 0
print(main(nth))
