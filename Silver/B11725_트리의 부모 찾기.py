import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n+1)]
parents = [0]*(n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(tree, start, parents):
    for i in tree[start]:
        if parents[i] == 0:
            parents[i] = start
            dfs(tree, i, parents)


dfs(tree, 1, parents)
for i in range(2, len(parents)):
    print(parents[i])
