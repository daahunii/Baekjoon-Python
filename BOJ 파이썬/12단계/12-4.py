# 체스판 다시 칠하기 (1018번) -> 해결 x
# 코드 참고 블로그 : https://real-myeong.tistory.com/49 (행열로 접근)
n, m = map(int, input().split())
board = []
count = []

for _ in range(n):
    board.append(input())

for a in range(n-7):
    for b in range(m-7):
        black = 0
        white = 0
    for i in range(a, a+8):
        for j in range(b, b+8):
            if (i+j)%2 == 0:
                if board[i][j] != 'W': white += 1
                if board[i][j] != 'B': black += 1
            else:
                if board[i][j] != 'B': white += 1
                if board[i][j] != 'W': black += 1
    count.append(black)
    count.append(white)
print(min(count))


