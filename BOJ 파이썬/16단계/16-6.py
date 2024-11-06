# 큐 2 (18258번)
import sys
N = int(sys.stdin.readline())
q = []
for _ in range(N):
    inst = list(sys.stdin.readline().split())
    if inst[0] == 'push': q.append(int(inst[1]))
    elif inst[0] == 'pop':
        if q:
            print(q[0])
            q.remove(q[0])
        else: print(-1)
    elif inst[0] == 'front':
        if q: print(q[0])
        else: print(-1)
    elif inst[0] == 'back':
        if q: print(q[-1])
        else: print(-1)
    elif inst[0] == 'size': print(len(q))
    elif inst[0] == 'empty':
        if q: print(0)
        else : print(1)

#==================================================
# 위 코드는 맞긴하나 시간초과 => 리스트에서 pop이 O(n)의 계산량을 요구해 시간이 초과됨
# 해결책으로 deque를 사용하면 됨 *deque란 양방향 자료형으로 stack처럼도 사용가능하고 queue로도 가능함
import sys
from collections import deque
n = int(input())
queue = deque([])
for i in range(n):
    com = sys.stdin.readline().split()
    if com[0] == 'push':
        queue.append(com[1])
    elif com[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif com[0] == 'size':
        print(len(queue))
    elif com[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif com[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif com[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])