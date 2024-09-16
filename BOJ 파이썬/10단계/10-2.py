# 직사각형에서 탈출 (1085번)

A, B, w, h = map(int, input().split())
print(min(A,B,w-A,h-B))