# 개수 세기 (10807번)
n = int(input())
nums = list(map(int, input().split()))
v = int(input())

if v in nums: print(nums.count(v))
else: print(0)