# 크로아티아 알파벳 (2941번)
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()
for i in range(len(croatia)):
    if croatia[i] in s:
        s = s.replace(croatia[i],'*') #크로아티아 문자들을 *로 다 바꾼다
print(len(s))