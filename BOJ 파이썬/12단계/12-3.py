# 수학은 비대면강의입니다 (19532번)
# 입력: a,b,c,d,e,f (-999~999)
# 출력: x,y
# 문제 : ax+by=c, dx+ey=f의 연립방정식

#sol1 (연립방정식 공식)
a,b,c,d,e,f = map(int, input().split())
print((c*e-b*f)//(a*e-b*d), (a*f-d*c)//(a*e-b*d))

#sol2 (브루트포스)
a,b,c,d,e,f = map(int, input().split())
for i in range(-999, 1000):
    for j in range(-999, 1000):
        if (a*i)+(b*j) == c and (d*i)+(e*j) == f: print(i,j)
