# 배수와 약수 (5086번)

while True:
    n1, n2 = map(int, input().split())
    if n1 < n2:
        if n2%n1 == 0: print("factor")
        else: print("neither")
    elif n1 > n2:
        if n1%n2 == 0: print("multiple")
        else: print("neither")
    else:
        break

    