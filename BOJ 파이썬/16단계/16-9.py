# 덱 2 (28279번)
import sys
from collections import deque
N = int(sys.stdin.readline())
d = deque([])
for _ in range(N):
    com = sys.stdin.readline().split()
    if com[0] == '1': d.appendleft(int(com[1]))
    elif com[0] == '2': d.append(int(com[1]))
    elif com[0] == '3':
        if d:
            print(d[0])
            d.popleft()
        else: print(-1)
    elif com[0] == '4':
        if d:
            print(d[-1])
            d.pop()
        else: print(-1)
    elif com[0] == '5': print(len(d))
    elif com[0] == '6':
        if d: print(0)
        else: print(1)
    elif com[0] == '7':
        if d: print(d[0])
        else: print(-1)
    elif com[0] == '8':
        if d: print(d[-1])
        else: print(-1)
