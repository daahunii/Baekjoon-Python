# 수 정렬하기3 (10989번)
# import sys

# N = int(input())
# arr = []
# for i in range(N):
#     arr.append(int(sys.stdin.readline())) # input은 속도가 느려 stdin.readline으로 입력
# arr.sort()
# for i in arr:
#     print(i)

# 위 코드는 메모리초과....
import sys
N = int(sys.stdin.readline())
arr = [0] * 10001 # 공간할당을 해서 메모리 초과를 피해보자....(10000개까지 입력 가능)

for i in range(N):
    arr[int(sys.stdin.readline())] += 1 # arr[i]++ 하면서 한줄씩 입력

for i in range(10001):
    if arr[i] != 0: # 앞에서부터 탐색하면서 공간을 쓴 곳까지 찾기 (0이 나오면 쓰지 않은 공간)
        for j in range(arr[i]):
            print(i)
