# 상수 (2908번)

a, b = input().split()
a = a[::-1]
b = b[::-1]
if int(a) > int(b): print(int(a))
else: print(b)