from sys import stdin

pts = [set(), set()]

for _ in range(3):
    a, b = map(int, stdin.readline().split())
    if a in pts[0]:
        pts[0].remove(a)
    else:
        pts[0].add(a)
    if b in pts[1]:
        pts[1].remove(b)
    else:
        pts[1].add(b)

print(f'{pts[0].pop()} {pts[1].pop()}')


'''
더 간단한 방법: XOR 사용하기
정수 n에 대해 
n^n = 0, 0^n=n
'''