# 세로 읽기 (10798번)

s = []
m = 0 #가장 긴 문자열 길이
for i in range(5):
    w = input()
    if len(w) >= m: m = len(w)
    s.append(w)

for i in range(m):
    for j in range(5):
        if i < len(s[j]): print(s[j][i], end='') # 최대 길이보다 작거나 같으면 출력