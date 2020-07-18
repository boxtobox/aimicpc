import sys
sys.setrecursionlimit(2000000000)
N = int(input())
counts = [0] * (N+1)
definite_answers = [1]

i, j = 0, 0
while 2**i <= N:
    j = 0
    while 2**i * 3**j <= N:
        definite_answers.append(2**i * 3**j)
        counts[2**i * 3**j] = i + j
        j += 1
    i += 1


def calc_routes(n):
    if n == 1:
        return 0
    if counts[n]:
        return counts[n]
    if n-1 in definite_answers:
        result = calc_routes(n-1) + 1
        counts[n] = result
        return result
    possible_routes = [calc_routes(n-1)]
    if not n % 2:
        if n // 2 in definite_answers:
            result = calc_routes(n//2) + 1
            counts[n] = result
            return result
        possible_routes.append(calc_routes(n // 2))
    if not n % 3:
        if n // 3 in definite_answers:
            result = calc_routes(n//3) + 1
            counts[n] = result
            return result
        possible_routes.append(calc_routes(n // 3))

    result = min(possible_routes) + 1
    counts[n] = result
    return result


for i in range(2, N+1):
    if counts[i]:
        print(i, counts[i])
print(calc_routes(N))
