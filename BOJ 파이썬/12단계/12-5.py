# 영화감독 숌 (1436번)
# 666이 무조건 들어가는데 최솟값부터... 오름차순?
# 666, 1666, 2666, 3666,...9666 다음은? 6660, 6661,...6669, 다음은? 
#  1,    2,    3,    4, ... 8,          9,    10,     18
# 와씨... 이렇게 풀면 절대 안될 것 같고 666이 포함될 때를 카운트해야하나...?

n = int(input()) # n번째 666포함 숫자
cnt = 0
num = 666 # 666부터 시작
while True:
    if '666' in str(num): cnt += 1
    if cnt == n:
        break
    num += 1
print(num)