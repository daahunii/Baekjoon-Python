# 대칭 차집합 (1269번)
import sys
A, B = map(int, sys.stdin.readline().split())
set_a = set(map(int, sys.stdin.readline().split()))
set_b = set(map(int, sys.stdin.readline().split()))
print(len(set_a - set_b) + len(set_b - set_a))