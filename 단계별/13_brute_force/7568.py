from sys import stdin


'''
5명인 경우, 중복 비교를 하지 않기 위해  
1: 2~5 와 비교
2: 3~5 .. 
3: 4~5 .. 
4: 5 ..

비교한 결과를 저장. 
a의 비교 결과: [0, 1, 0, 1, 0] 0: a보다 더 크지 않음. 1: a보다 더 큼
'''


def compare(x, y, p, q):
    if x < p and y < q:
        return 1
    else:
        return 0


N = int(stdin.readline())
body_data = []
compare_list = [0] * N
for _ in range(N):
    body_data.append(tuple(map(int, stdin.readline().split())))

for i in range(0, N):
    for j in range(0, N):
        if compare(*(body_data[i] + body_data[j])):
            compare_list[i] += 1

print(' '.join([f'{k+1}' for k in compare_list]))


