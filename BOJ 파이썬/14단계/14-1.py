# 숫자 카드 (10815번)
# import sys
# N = int(sys.stdin.readline())
# n_arr = list(map(int, sys.stdin.readline().split()))
# M = int(sys.stdin.readline())
# m_arr = list(map(int, sys.stdin.readline().split()))

# result = []
# for i in range(len(m_arr)):
#     flag = 0
#     for j in range(len(n_arr)):
#         if n_arr[j] == m_arr[i]:
#             flag = 1 # 숫자가 포함되어 있으면 flag가 1이 되고
#             result.append(1)
#     if flag == 0: # 숫자가 포함되지 않았으면 0 추가
#         result.append(0)
# for i in range(len(result)):
#     print(result[i], end=' ')

#=========================================
# 위에 풀이는 답은 맞지만 시간 초과가 남 => 딕셔너리로 풀어서 시간 단축 or 다른 방법....(이진탐색)

import sys
N = int(sys.stdin.readline())
n_arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
m_arr = list(map(int, sys.stdin.readline().split()))

result = {} # 시간단축을 위해 딕셔너리로 선언
for i in m_arr:
    result[i] = 0 # 비교하기 전 0으로 모두 맵핑
for j in n_arr:
    if j in result: result[j] = 1 # n개의 카드에서 같은 수가 있으면 1로 바꿈

for i in result:
    print(result[i], end=' ')

#=========================================
# 이진탐색 풀이법 (다른 사람 풀이 참고)
n = int(input())
N = list(map(int, input().split()))
m = int(input())
M = list(map(int, input().split()))
N.sort()

def bs(x):
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        if N[mid] == x: return 1
        elif x < N[mid]: high = mid - 1
        else: low = mid + 1
    return 0

for i in M:
    print(bs(i), end=' ')