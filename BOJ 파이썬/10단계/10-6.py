# 삼각형 외우기 (10101번)
angle = []
for i in range(3):
    n = int(input())
    angle.append(n)

if sum(angle) != 180: print("Error")
else:
    if angle[0] == angle[1] == angle[2] :print("Equilateral")
    elif angle[0] == angle[1] or angle[1] == angle[2] or angle[2] == angle[0]: print("Isosceles")
    elif angle[0] != angle[1] and angle[1] != angle[2]: print("Scalene")