# 소트인사이드 (1427번)
n = int(input())
arr = []
for i in str(n):
    arr.append(int(i))
arr.sort(reverse=True)
for i in arr:
    print(i, end='')