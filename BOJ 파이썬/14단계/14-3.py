# 회사에 있는 사람 (7785번)
import sys
n = int(sys.stdin.readline().strip())
info = {}
for _ in range(n):
    name, act = sys.stdin.readline().strip().split()
    if act == 'enter': info[name] = act
    else: info.pop(name)

info = sorted(info.keys(), reverse=True) # 사전상 역순으로 출력해야하므로
for i in info:
    print(i)