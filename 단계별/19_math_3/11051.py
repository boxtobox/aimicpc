# 이항계수 2

import sys
sys.setrecursionlimit(1500)
combs = [[1 if (j == 0 or j == k) else 0 for j in range(k+1)] for k in range(1001)]
MOD = 10007


def comb(n, k):
    assert n >= k, k >= 0
    if combs[n][k]:
        return combs[n][k]
    else:
        result = (comb(n-1, k) % MOD + comb(n-1, k-1) % MOD) % MOD
        combs[n][k] = result
        return result


N, K = map(int, input().split())
print(comb(N, K))
