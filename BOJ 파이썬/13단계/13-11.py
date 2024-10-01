# 좌표 압축 (18870번)
# key(원래숫자 = n_sort[i]):value(인덱스 = i)로 mapping
import sys
N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

n_sort = sorted(set(num))
d = {}
for i in range(len(n_sort)):
    d[n_sort[i]] = i # 정렬한 인덱스번호가 자신보다 작은 숫자의 개수이므로 key(원래숫자):value(인덱스)로 mapping
for i in num:
    print(d[i], end=" ") 
