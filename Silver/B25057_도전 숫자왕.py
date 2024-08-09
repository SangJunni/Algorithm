from itertools import combinations
n = int(input())
nums = list(map(int, input().split()))
result = set()
for i in range(1,n+1):
    for case in combinations(nums,i):
        result.add(sum(case))
print(sum(nums) - len(result))