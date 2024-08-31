# 최댓값 (2566번)
m = 0
point = []

for i in range(9):
    num = [*map(int, input().split())]
    for j in range(9):
        if num[j] >= m:
            m = num[j]
            point = [i+1, j+1]
print(m)
for i in range(2): print(point[i], end=' ')