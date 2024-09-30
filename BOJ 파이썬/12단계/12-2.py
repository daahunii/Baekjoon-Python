# 분해합 (2231번)
# 내 풀이는 out of range로 인해... 실패
N = int(input())
flag = 0 # 분해합이 있으면 1, 없으면 0
start = N - len(str(N))*9 # 각 자리별로 0~9가 들어가는데 9가 최대이므로 9x자릿수를 입력값에서 빼면 시작점을 정할 수 있다! 
if start <= 0: flag = 0
else:
    for i in range(start,N):
        s = i
        for j in range(len(str(N))):
            s += ord(str(i)[j]) - ord('0') # 각 자릿수의 수를 문자열로 치환 -> 아스키 코드를 이용해 다시 숫자를 s에 대입해서 각 자리수를 더함; ord():문자->아스키코드

        if s == N:
            flag = 1
            print(i)
            break
if flag == 0: print(0)

#====================================
# map을 활용한 간단 풀이....
n = int(input())  # 분해합을 입력값으로 받음

for i in range(1, n+1):   # 해당 분해합의 생성자 찾기
    num = sum((map(int, str(i))))  # i의 각 자릿수를 더함
    num_sum = i + num  # 분해합 = 생성자 + 각 자릿수의 합
    # i가 작은 수부터 차례로 들어가므로 처음으로 분해합과 입력값이 같을때가 가장 작은 생성자를 가짐
    if num_sum == n:
        print(i)
        break
    if i == n:  # 생성자 i와 입력값이 같다는 것은 생성자가 없다는 뜻
        print(0)