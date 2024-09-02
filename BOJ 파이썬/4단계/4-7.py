# 과제 안 내신 분..? (5597번)

student = [0]*30
for i in range(30):
    student[i] = i+1

for i in range(28):
    n = int(input())
    for j in range(30):
        if n == student[j]:
            student[j] = 0

for i in range(30):
    if student[i] != 0: print(student[i])