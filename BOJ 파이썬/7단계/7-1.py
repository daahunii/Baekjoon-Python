# 행렬 덧셈 (2738번)
n, m = map(int, input().split())
a = []
b = []
for i in range(n):
    arr = [*map(int, input().split())]
    a.append(arr)

for i in range(n):
    arr = [*map(int, input().split())]
    b.append(arr)

for i in range(n):
    for j in range(m):
        print(a[i][j]+b[i][j], end=' ')
    print('')