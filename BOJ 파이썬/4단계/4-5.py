# 공 넣기 (10810번)

n, m = map(int , input().split())
box = [0]*n

for t in range(m):
    i, j, k = map(int, input().split())
    for idx in range(i, j+1):
        box[idx-1] = k #배열 특성상 인덱스가 0부터 시작하므로 idx-1

for i in range(n):
    print(box[i], end=" ")