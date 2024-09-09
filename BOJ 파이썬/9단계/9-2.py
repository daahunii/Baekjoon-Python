# 약수 구하기 (2501번)

N, K = map(int, input().split())
y = []
i = 1
while N != 0:
    if N % i == 0: y.append(i)
    i += 1
    if i == N:
        y.append(i)
        break
if K <= len(y): print(y[K-1])
else: print(0)