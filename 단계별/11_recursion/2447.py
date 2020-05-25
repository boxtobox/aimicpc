from sys import stdin


def sierpinski_carpet(n):
    carpet = ["#"]
    for i in range(n):
        carpet = [x + x + x for x in carpet] + \
                 [x + x.replace("#", " ") + x for x in carpet] + \
                 [x + x + x for x in carpet]
    return "\n".join(carpet)


N = int(stdin.readline())
print(sierpinski_carpet(N))
# https://rosettacode.org/wiki/Sierpinski_carpet#Python
