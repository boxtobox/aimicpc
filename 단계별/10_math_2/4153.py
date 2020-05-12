from sys import stdin

while 1:
    lines = sorted(list(map(int, stdin.readline().split())))
    if not lines[-1]:
        break
    if lines[-1]**2 == lines[0]**2 + lines[1]**2:
        print("right")
    else:
        print("wrong")
