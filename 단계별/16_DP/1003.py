fib_memo = [(1, 0), (0, 1)]


def fib(n: int) -> tuple:
    if len(fib_memo) > n:
        return fib_memo[n]
    else:
        result = (fib(n-1)[0] + fib(n-2)[0], fib(n-1)[1] + fib(n-2)[1])
        fib_memo.append(result)
        return result


N = int(input())
for _ in range(N):
    i, j = fib(int(input()))
    print(i, j)
