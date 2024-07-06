from itertools import permutations
n = int(input())
nums = sorted([int(input()) for _ in range(n)])
result = [int(str(x)+str(y)) for x,y in permutations(nums[:4], 2)]
result.sort()
print(result[2])