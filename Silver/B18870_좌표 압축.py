import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
s_data = sorted(list(set(data)))
dict = {s_data[i]: i for i in range(len(s_data))}
for d in data:
    print(dict[d], end=' ')
#.index의 시간복잡도는 O(N)을 가짐
# 집합을 사용해서 문제 해결하기





