# 공 바꾸기 (10813번)

n, m = map(int, input().split())

box = [0]*n
for i in range(n):
    box[i] = i+1

for t in range(m):
    tmp = 0
    i, j = map(int, input().split())
    tmp = box[i-1]
    box[i-1] = box[j-1]
    box[j-1] = tmp

for i in range(n):
    print(box[i], end=" ")