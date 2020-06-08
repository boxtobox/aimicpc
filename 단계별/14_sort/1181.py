from sys import stdin, stdout

read = stdin.readline
N = int(read())
words = {(read().rstrip()) for _ in range(N)}
words = sorted(list(words), key=lambda k: (len(k), k))
stdout.write('\n'.join(words))
