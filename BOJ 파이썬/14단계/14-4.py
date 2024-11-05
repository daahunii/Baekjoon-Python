# 나는야 포켓몬 마스터 이다솜 (1620번)
import sys
N, M = map(int, sys.stdin.readline().split())
pokemon = {}
for n in range(N):
    p = sys.stdin.readline().strip()
    pokemon[p] = str(n+1) # 포켓몬이름-도감번호 맵핑해서 저장

test = []
for m in range(M): # 문제 출제
    test.append(sys.stdin.readline().strip()) 

for i in range(M):
    if test[i] in pokemon.keys(): # 포켓몬 이름이 입력 되었을 경우
        print(pokemon[test[i]]) # 도감번호 출력
    elif test[i] in pokemon.values(): # 도감번호가 입력 되었을 경우
        for k,v in pokemon.items(): # 이름 출력
            if v == test[i]: print(k)

#===============================
# 위 코드도 맞긴한데 이중for문 때문에 시간초과 발생....ㅠㅠ
# 단일 for문을 쓸 수 있게 만들어야할 듯 (딕셔너리를 포켓몬용, 번호용 따로 만들기)

import sys
N, M = map(int, sys.stdin.readline().split())
pokemon = dict()
number = dict()
for i in range(1, N+1):
    p = sys.stdin.readline().strip()
    pokemon[i] = p # O(N)
    number[p] = i

for i in range(M):
    find = sys.stdin.readline().strip()
    if find[0].isalpha():
        print(number[find]) # O(N^2)
    else:
        print(pokemon[int(find)])