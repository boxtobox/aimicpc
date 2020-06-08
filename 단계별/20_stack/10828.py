'''
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.'''
from sys import stdin
read = stdin.readline


class Stack:
    def __init__(self):
        self.items = []

    def push(self, i):
        self.items.append(i)

    def pop(self):
        if self.size() == 0:
            return -1
        else:
            return self.items.pop()

    def size(self):
        return self.items.__len__()

    def empty(self):
        return int(self.size() == 0)

    def top(self):
        if self.size() == 0:
            return -1
        else:
            return self.items[-1]


stack = Stack()
N = int(read())
for _ in range(N):
    cmd = read().split()
    if cmd[0] == 'push':
        stack.push(int(cmd[1]))
    elif cmd[0] == 'pop':
        print(stack.pop())
    elif cmd[0] == 'size':
        print(stack.size())
    elif cmd[0] == 'empty':
        print(stack.empty())
    elif cmd[0] == 'top':
        print(stack.top())



