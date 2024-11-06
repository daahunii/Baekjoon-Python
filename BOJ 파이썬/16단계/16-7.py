# 카드2 (2164번)
from collections import deque
N = int(input())
cards = deque([])
for i in range(N):
    cards.append(i+1)
while len(cards) > 1:
    # print(cards)
    cards.popleft()
    cards.rotate(-1)
print(cards[0])