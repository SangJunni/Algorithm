n = int(input())
for _ in range(n):
    a,b = map(float, input().split())
    print(f'{abs(a-b):.1f}')