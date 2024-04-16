n = int(input())
for _ in range(n):
    sacks = list(map(int, input().split()))
    print(f'Case #{_+1}: {max(sacks)}')