# 서로 다른 부분 문자열의 개수 (11478번)
import sys
S = sys.stdin.readline().strip()
s_list = set()
for i in range(len(S)):
    for j in range(i, len(S)):
        s_list.add(S[i:j+1])
print(len(s_list))