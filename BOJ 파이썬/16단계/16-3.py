# 괄호 (9012번)
T = int(input())

for _ in range(T):
    stack = []
    p = input() # 괄호들
    for i in p:
        if i == '(': stack.append(i)
        elif i == ')': 
            if stack: stack.pop() # stack 내 괄호가 있으면 pop
            else:
                print("NO")
                break
    else:
        if not stack: # break 안 걸리고 stack이 비어있으면 짝이 맞음
            print("YES")
        else: print("NO")