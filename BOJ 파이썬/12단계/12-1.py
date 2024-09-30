# 블랙잭 (2798번)
N, M = map(int, input().split()) # 카드갯수, 만들어야 하는 숫자
num_list = list(map(int, input().split()))
result = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if num_list[i]+num_list[j]+num_list[k] > M:
                continue
            else:
                result = max(result, num_list[i]+num_list[j]+num_list[k]) # 기존에 저장한 값과 다르게 뽑은 값과 비교해 최댓값 업데이트
print(result)