def fib(n):
    alpha = (1 + 5 ** 0.5) / 2
    beta = (1 - 5 ** 0.5) / 2
    a = 1 / 5 ** 0.5

    return int(a * (alpha**n - beta**n))


N = int(input())
print(fib(N))
# for i in range(0, 100):
#     print(fib(i))

