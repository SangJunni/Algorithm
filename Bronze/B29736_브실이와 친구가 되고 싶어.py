a, b = map(int, input().split())
k, x = map(int, input().split())
friends = [i for i in range(a,b+1) if (k-x <= i <= k+x)]
print(len(friends) if len(friends) != 0 else 'IMPOSSIBLE')
