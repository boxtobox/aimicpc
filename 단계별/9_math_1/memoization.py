from timing_2 import check_time


# iterative
def fib_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        fn = 0
        fn1 = 1
        fn2 = 2
        for i in range(3, n):
            fn = fn1 + fn2
            fn1 = fn2
            fn2 = fn1
        return fn


# recursive
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


__fib_cache = {}


def fib_memo(n):
    if n in __fib_cache:
        return __fib_cache[n]

    else:
        __fib_cache[n] = n if n < 2 else fib_memo(n-2) + fib_memo(n-1)
        return __fib_cache[n]



@check_time
def main():
    print(fib_memo(1000))


if __name__ == '__main__':
    main()