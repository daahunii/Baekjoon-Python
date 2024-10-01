# 수 정렬하기2 (2751번)
import sys

N = int(input())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline())) # input은 속도가 느려 stdin.readline으로 입력
arr.sort()
for i in arr:
    print(i)