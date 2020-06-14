fib_cache = [0, 1]


def fib(n):
    if len(fib_cache) > n:
        return fib_cache[n]
    else:
        result = fib(n-1) + fib(n-2)
        fib_cache.append(result)
        return result

fib(10)
print(fib_cache)