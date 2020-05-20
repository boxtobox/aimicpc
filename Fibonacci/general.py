def fib(n):
    alpha = (1 + 5 ** 0.5) / 2
    beta = (1 - 5 ** 0.5) / 2
    a = 1 / 5 ** 0.5

    return a * (alpha**n - beta**n)

for i in range(1, 100):
    print(fib(i))

