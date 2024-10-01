# 좌표 정렬하기2 (11651번) - y기준 정렬
import sys
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    [x,y] = map(int, sys.stdin.readline().split())
    arr.append([y,x])
arr.sort()
for i in arr: print(i[1], i[0]) # i[1]=x, i[0]=y