# 삼각형과 세 변 (5073번)
while True :
  a, b, c = map(int, input().split())
  if a == b == c == 0 : break
  if max((a, b, c)) >= sum((a, b, c)) - max((a, b, c)) : print("Invalid")
  elif a == b == c : print('Equilateral')
  elif a == b or b == c or a == c : print("Isosceles")
  else : print("Scalene")