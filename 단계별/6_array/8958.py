import sys

N = int(sys.stdin.readline())

for _ in range(N):
    OX_result = sys.stdin.readline().rstrip()
    streak = 0
    score = 0
    for result in OX_result:
        if result == 'X':
            score += (streak * (streak + 1)) / 2
            streak = 0
        elif result == 'O':
            streak += 1
        else:
            raise ValueError

    if streak:
        score += (streak * (streak + 1)) / 2

    print(int(score))
