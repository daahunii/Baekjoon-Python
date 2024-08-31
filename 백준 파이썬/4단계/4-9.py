# 바구니 뒤집기 (10811번)

n, m = map(int, input().split())
# box = [0]*n
# for i in range(n):
#     box[i] = i+1
box = [i for i in range(1,n+1)]
tmp = 0
for t in range(m):
    i, j = map(int, input().split())
    for idx in range(i, j):
        tmp = box[i-1:j]
        tmp.reverse()
        box[i-1:j] = tmp

for i in range(n):
    print(box[i], end=" ")