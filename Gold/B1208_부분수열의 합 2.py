import sys
from itertools import combinations
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
n, m = map(int, input().split())
sequence = list(map(int, input().split()))

def getCases(sequence, result):
    for i in range(1, len(sequence)+ 1):
        for comb in combinations(sequence, i):
            result.append(sum(comb))
    result.sort()

left, right = sequence[:n//2], sequence[n//2:]
lSum, rSum = [], []
getCases(left, lSum)
getCases(right, rSum)
answer = 0
for l in lSum:
    r = m - l
    answer += bisect_right(rSum, r) - bisect_left(rSum, r)
answer += bisect_right(lSum, m) - bisect_left(lSum, m)
answer += bisect_right(rSum, m) - bisect_left(rSum, m)
print(answer)
