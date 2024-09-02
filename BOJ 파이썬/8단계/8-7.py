# 달팽이는 올라가고 싶다 (2869번)
# 낮에 올라가는 거리 : A미터, 밤에 미끄러지는 거리 : B미터, 나무막대 높이 : V미터
# 시간 제한이 0.25초이므로 반복문X -> 모듈로 연산(나머지) 사용
# 올라가야 할 거리 : V-B, 하루에 올라갈 수 있는 거리 : A-B
import math
A, B, V = map(int, input().split())
days = (V-B)/(A-B)
print(math.ceil(days)) #ceil함수 : 올림시켜줌