# 그대로 출력하기 (11718번)
import sys

while True:
    try:
        print(input())
    except EOFError: #End of File Error(파일에서 더 이상 읽을 내용이나 입력 값이 없을 때 발생)
        break