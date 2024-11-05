# 듣보잡 (1764번)
import sys
N, M = map(int, sys.stdin.readline().split())
a=set() # set을 이용해 중복 제거
b=set()
result =[]
for _ in range(N): # 듣도 못한 사람
    a.add(sys.stdin.readline().strip())
for _ in range(M): # 보도 못한 사람
    b.add(sys.stdin.readline().strip())

for i in a:
    if i in b: result.append(i) # 겹치면 추가
result.sort() # 사전상 오름차순
print(len(result))
for i in result : print(i)