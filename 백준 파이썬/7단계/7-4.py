# 색종이 (2563번)

n = int(input()) # 색종이 수
paper = [[0]*100 for _ in range(100)] # 도화지 100x100 0으로 초기화 (색종이가 붙혀진 부분은 1로 바꿈)
for i in range(n):
    x, y = map(int, input().split()) # 각 색종이별 왼쪽 아래 좌표
    for j in range(y, y+10): # 세로부터
        for k in range(x, x+10): # 가로로 1 만들어주기
            paper[j][k] = 1

s = 0 # 최종 넓이
for i in range(100): # 도화지 전체를 탐색
    s += paper[i].count(1) # 숫자 1만 카운트
print(s)