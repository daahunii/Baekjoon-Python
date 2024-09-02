# 세탁소 사장 동혁 (2720번)

T = int(input())
result = []
for i in range(T):
    cent = int(input())
    case = []
    if cent >= 25:
        case.append(cent//25)
        cent %= 25
    else: case.append(0)
    if cent >= 10:
        case.append(cent//10)
        cent %= 10
    else: case.append(0)
    if cent >= 5:
        case.append(cent//5)
        cent %= 5
    else: case.append(0)
    if cent >= 1:
        case.append(cent//1)
        cent %= 1
    else: case.append(0)
    result.append(case)

for i in range(T):
    for j in range(4): print(result[i][j], end=' ')
    print('')