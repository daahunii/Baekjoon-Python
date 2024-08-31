# 문자열 (9086번)
t = int(input())
result = []
for i in range(t):
    word = input()
    result.append(word[0]+word[-1])
for i in range(t): print(result[i])