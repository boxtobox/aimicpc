from sys import stdin

# Timsort is stable
N = int(stdin.readline())
users = [(int(a), b) for a, b in [stdin.read().splitlines(True).rstrip().split(' ')]]
users = sorted(users, key=lambda x: x[0])
print(users)
for user in users:
    print(user[0], user[1])

print(['%d %s' % (user[0], user[1])] for user in users)


