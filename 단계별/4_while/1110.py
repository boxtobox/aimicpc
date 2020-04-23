import sys


def new_num(n):
    if n < 10:
        result = n * 10 + n
    else:
        c, d = n // 10, n % 10
        result = d * 10 + (c + d) % 10
    return result


if __name__ == '__main__':
    num = int(sys.stdin.readline())
    first_num = num
    cycle = 0
    condition = False

    while not condition:
        num = new_num(num)
        cycle += 1
        condition = (num == first_num)

    print(cycle)
