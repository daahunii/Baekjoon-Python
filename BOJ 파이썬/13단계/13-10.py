# 나이순 정렬 (10814번)

N = int(input())
arr = []
for _ in range(N):
    [age,name] = map(str, input().split())
    arr.append([int(age),name])

arr.sort(key= lambda x: x[0]) # age만 정렬
for i in arr:
    print(i[0],i[1])