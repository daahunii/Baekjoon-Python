# 네 번째 점 (3009번)
pointX = []
pointY = []
for i in range(3):
    x, y = map(int, input().split())
    pointX.append(x)
    pointY.append(y)

for i in range(3):
    if pointX.count(pointX[i]) == 1: px4 = pointX[i]
    if pointY.count(pointY[i]) == 1: py4 = pointY[i]
print(px4,py4)