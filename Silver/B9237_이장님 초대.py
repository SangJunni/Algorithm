n = int(input())
trees = sorted(list(map(int, input().split())), reverse=True)
growth = [x+trees[x]+2 for x in range(n)]
print(max(growth))