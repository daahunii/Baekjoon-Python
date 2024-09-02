# 곱셈 (2588)
a = int(input())
b = int(input())
tmp = []
while True: #tmp리스트에 자릿수 나눠 담기
    tmp.append(b%10)
    b = b//10
    if b==0: break

result = 0
for i in range(3):
    result += a*tmp[i]*10**i #왼쪽으로 이동하면서 더해야함 
    print(a*tmp[i])
print(result)
#print(a*b)를 하면 되는거 아닌가? 굳이 result를 왜 만들지? -> 위에 반복문을 통해 b의 값은 0이 되어있는 상태!


#=====================================================
#더 간단한 풀이

a = int(input())
b = input() # 두번째 숫자를 문자열로 받아서!

for i in range(3, 0, -1):
    print(a*int(b[i-1])) # 반목문 안에서 정수로 변환시켜 곱한다
print(a*int(b)) #b의 변형 없이 정수로 바로 바꿔 출력

