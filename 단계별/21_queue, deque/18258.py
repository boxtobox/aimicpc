'''
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''

from sys import stdin
read = stdin.readline


class Queue:
    def __init__(self):
        self.items = []
        self.idx = 0
        self.sizeof = 0

    def size(self):
        return self.sizeof

    def push(self, i):
        self.items.append(i)
        self.sizeof += 1

    def pop(self):
        if self.size() == 0:
            return -1
        result = self.items[self.idx]
        self.idx += 1
        self.sizeof -= 1
        return result

    def empty(self):
        return int(self.size() == 0)

    def back(self):
        if self.size():
            return self.items[-1]
        else:
            return -1

    def front(self):
        if self.size():
            return self.items[self.idx]
        else:
            return -1


queue = Queue()
N = int(read())
for _ in range(N):
    cmd = read().split()
    if cmd[0] == 'push':
        queue.push(int(cmd[1]))
    elif cmd[0] == 'pop':
        print(queue.pop())
    elif cmd[0] == 'size':
        print(queue.size())
    elif cmd[0] == 'empty':
        print(queue.empty())
    elif cmd[0] == 'front':
        print(queue.front())
    elif cmd[0] == 'back':
        print(queue.back())



