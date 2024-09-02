# 진법 변환2 (11005번)

N, B = map(int, input().split()) # 60466175, 36 => N을 B로 나누고 나머지들을 다 이어붙이면..?
num = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" # num[35] = Z
result = ''

while N!=0:
    result += num[N%B] # 다 이어붙이고 나서 마지막에 뒤집어야함
    N //= B # '//'기호는 몫만 남김
print(result[::-1])