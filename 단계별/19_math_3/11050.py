# 이항계수 1


def comb(n, k):
    assert n >= k, k >= 0
    if n == k or k == 0:
        return 1
    else:
        return comb(n-1, k) + comb(n-1, k-1)


N, K = map(int, input().split())
print(comb(N, K))