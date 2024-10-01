# 단어 정렬 (1181번)
# N = int(input())
# words = []
# max_len = 0
# for _ in range(N):
#     words.append(input())
# check_words = list(set(words)) # set으로 중복 제거

# for i in check_words: # 가장 긴 단어의 길이
#     if max_len <= len(i): max_len = len(i)

# check_words.sort()  # 사전 순 정렬
# result = []
# for i in range(1, max_len+1): # 길이 순으로 정렬하고 result에 담기
#     for j in check_words:
#         if len(j) == i:
#             result.append(j)
# for word in result:
#     print(word)



# 다른 풀이 sort 람다식 사용
# 참고 블로그 : https://kingofbackend.tistory.com/98
N = int(input())
words = []
for _ in range(N):
    words.append(input())
#중복 제거
data_list = list(set(words))

data_list.sort()
data_list.sort(key=lambda x : len(x))

for word in data_list:
    print(word)