'''
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''

from sys import stdin
MAX_SIZE = 2000000
MAX_SIZE = 4
read = stdin.readline


class Queue:
    def __init__(self):
        self.items = [None] * MAX_SIZE
        self.start = 0
        self.end = 0
        self.sizeof = 0

    def size(self):
        print(self.sizeof)
        return

    def push(self, i):
        if self.sizeof == 0:
            self.start = self.end = 0
            self.items[self.end] = i
        else:
            if self.end == MAX_SIZE - 1:
                self.end = 0
            else:
                self.end += 1
            self.items[self.end] = i
        self.sizeof += 1

    def pop(self):
        if self.size() == 0:
            print(-1)
            return
        result = self.items[self.start]
        if self.start == MAX_SIZE - 1:
            self.start = 0
        else:
            self.start += 1
        self.sizeof -= 1
        print(result)
        return

    def empty(self):
        print(int(self.size() == 0))
        return

    def back(self):
        if self.size():
            print(self.items[self.end])
            return
        else:
            print(-1)
            return

    def front(self):
        if self.size():
            print(self.items[self.start])
            return
        else:
            print(-1)
            return


queue = Queue()
N = int(read())
for _ in range(N):
    cmd = read().split()
    if cmd[0] == 'push':
        queue.push(int(cmd[1]))
    elif cmd[0] == 'pop':
        queue.pop()
    elif cmd[0] == 'size':
        queue.size()
    elif cmd[0] == 'empty':
        queue.empty()
    elif cmd[0] == 'front':
        queue.front()
    elif cmd[0] == 'back':
        queue.back()


