# 문자열 집합 (14425번)

N,M = map(int, input().split())
s = []
str_set = []
for _ in range(N): # 문자열 집합 s 만들기
    s.append(input()) 

for _ in range(M): # 집합 s와 비교할 대상 문자리스트
    str_set.append(input())

cnt = 0
for i in str_set:
    if i in s: cnt += 1
print(cnt)