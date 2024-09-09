# 소수 (2581번)
M = int(input())
N = int(input())
n_list = [] # M과 N사이의 값들
prime = [] # 소수를 담을 리스트

for i in range(M, N+1): n_list.append(i)
for i in n_list:
    p = [] # 약수를 담을 리스트
    for j in range(1,i+1):
        if i%j == 0: p.append(j)
    if len(p) == 2: prime.append(i)

if len(prime) == 0: print(-1)
else:
    print(sum(prime)) # 합
    print(prime[0]) # sorting 되어 있으므로 인덱스 0번이 최솟값