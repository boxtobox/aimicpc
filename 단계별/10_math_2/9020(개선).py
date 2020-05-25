from sys import stdin

LIMIT = 10000


def find_primes(limit):
    length = int(limit ** 0.5)
    sieve = [1] * (limit + 1)
    sieve[0:2] = 0, 0
    for i in range(2, length + 1):
        if sieve[i]:
            sieve[i * 2::i] = [0] * (limit // i - 1)
    return sieve


primes = find_primes(LIMIT)
TestCase = int(stdin.readline())
for _ in range(TestCase):
    odd_num = int(stdin.readline())
    for k in range(odd_num//2, 0, -1):
        if primes[k] and primes[odd_num-k]:
            print(f'{k} {odd_num-k}')
            break



'''
골드바흐 파티션 찾기(10000 이하의 짝수)
1. 10000 이하의 짝수와 대응하는 리스트를 만든다. 각 원소는 없음
2. 10000 미만의 소수를 전부 찾아서 리스트로 만든다.
3. 그 중 2개를 골라 합을 구한다.
    2중 for 문 사용
    바깥: i:range(0, N), 안: j: j: range(i+1, N)
    안 loop 돌 때, 합이 10000 초과하면 바로 break 
4. 그 합에 해당하는 리스트 원소에 대해
4-1 만약 파티션이 없다면, 소수 두개를 원소로 넣음
4-2 만약 파티션이 이미 있다면, 소수 두개의 차를 비교해 더 적으면 넣고 많으면 패스


더 빠른 방법:
1. 길이 10001짜리 배열(primes)을 만들고, 인덱스가 소수면 1, 소수가 아니면 0을 입력한다.
2. 입력받은 짝수(= 2k)의 가장 차이가 작은 골드바흐 파티션 찾기:
2-1 k와 k가 소수? -> 파티션은 (k, k)
    else k-1 and k+1 소수? -> (k-1, k+1)
    else k-2 and k+2 소수? -> (k-2, k+2)
    ...반복

'''