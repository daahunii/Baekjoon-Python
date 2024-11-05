# 숫자 카드2 (10816번)
import sys
N = int(sys.stdin.readline())
n_arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
m_arr = list(map(int, sys.stdin.readline().split()))

result = {} # 시간단축을 위해 딕셔너리로 선언
for n in n_arr:
    if n in result: result[n] += 1 # 존재하면 +1
    else: result[n] = 1 # 없으면 추가 

for m in m_arr:
    if m in result: print(result[m], end=' ')
    else: print(0, end=' ')