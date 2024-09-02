# 진법 변환 (2745번)
# 첨에 이해 안되다가 https://growingarchive.tistory.com/208 여기 참고함

N, B = input().split() # ZZZZZ, 36
N = N[::-1]
B = int(B) 
num = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" # num[35] = Z
result = 0

for i in range(len(N)-1, -1, -1): # 지수가 3, 2, 1, 0 순으로...
    s = num.index(N[i]) * (B**i) # 35 * 36**지수
    result += s
print(result)