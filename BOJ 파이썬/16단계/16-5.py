# 도키도키 간식드리미 (12789번)
N = int(input())
num = list(map(int, input().split()))
stack = []
cnt = 1
for i in num:
    stack.append(i)
    while stack and stack[-1] == cnt: # stack이 비어있지 않고 top이 cnt와 같다면
        # print(stack)
        stack.pop()
        cnt += 1
if len(stack) == 0: print("Nice")
else: print("Sad")
