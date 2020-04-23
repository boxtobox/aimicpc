import sys

N = int(sys.stdin.readline())

for _ in range(N):
    scores = list(map(int, sys.stdin.readline().split()))[1:]
    avg = sum(scores) / len(scores)
    above_avg = 0
    for score in scores:
        if score > avg:
            above_avg += 1

    print('{:.3%}'.format((above_avg / len(scores))))
