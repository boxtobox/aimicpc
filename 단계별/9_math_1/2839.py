import sys

sugar = int(sys.stdin.readline())

p_5 = sugar//5
p_3 = 0
matched = False
for i in range(p_5, -1, -1):
    if (sugar - 5 * i) % 3 == 0:
        p_5 = i
        p_3 = (sugar - 5 * i) // 3
        matched = True
        break

if matched:
    total_p = p_5 + p_3
else:
    total_p = -1
print(total_p)
