# 소수 찾기 (1978번)
N = int(input())
n_list = list(map(int, input().split()))
prime = [] # 소수를 담을 리스트
for i in range(len(n_list)):
    p = [] # 약수를 담을 리스트
    for j in range(1, n_list[i]+1):
        if n_list[i]%j == 0: p.append(j)
    # print(p)
    if len(p) == 2: prime.append(n_list[i]) #소수는 자기자신과 1만을 약수로 가지므로 리스트 길이가 2

print(len(prime))