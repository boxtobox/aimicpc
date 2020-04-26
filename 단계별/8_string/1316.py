import sys

N = int(sys.stdin.readline())
result = 0

for _ in range(N):
    word = str(sys.stdin.readline().rstrip())
    i = 0
    w_s = set()
    is_group = True
    while i < len(word):
        ltr = word[i]
        if ltr in w_s:
            is_group = False
        while i < len(word) - 1 and word[i+1] == ltr:
            i += 1
        i += 1
        w_s.add(ltr)
    if is_group:
        result += 1

print(result)
