# 커트라인 (25305번)

N, k = map(int, input().split())
points = list(map(int, input().split()))
print(sorted(points)[-k]) # 오름차순 정렬이므로 우측에서부터 k번째가 커트라인