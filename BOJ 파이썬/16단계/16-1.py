# 스택 2 (28278번)
import sys
N = int(sys.stdin.readline())
s = []
def stack(i,v):
    if i==1:
        s.append(v)
    elif i==2:
        if len(s) == 0: print(-1)
        else: print(s.pop())
    elif i==3: print(len(s))
    elif i==4:
        if len(s) == 0: print(1)
        else: print(0)
    elif i==5:
        if len(s) == 0: print(-1)
        else: print(s[-1])
for _ in range(N):
    inst = list(map(int, sys.stdin.readline().split()))
    if len(inst) == 2: stack(inst[0], inst[1])
    else: stack(inst[0],0)