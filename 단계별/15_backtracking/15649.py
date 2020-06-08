# N, M = map(int, input().split())

route = []


def solve_comb(k, n, left):
    # k: 체크할 수, n: 최대값, left: 더 뽑아야 하는 수
    if left == 0:
        return True
    else:
        for i in range(k, max(n+1, n-left+2)):
            if solve_comb(i+1, n, left-1):
                route.append(i)
            else:
                return False


print(solve_comb(3, 5, 3))
print(route)

'''
Use mathematical induction to show that when n is an exact power of 2, the solution of the recurrence
T(n) = { 2          if n = 2,
       { 2T(n/2)    if n = 2^k, for k > 1
'''

