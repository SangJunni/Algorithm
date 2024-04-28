n = int(input())
answer = ['zilch', 'double', 'double-double', 'triple-double']
for _ in range(n):
    stats = list(map(int, input().split()))
    count = sum([1 if x >= 10 else 0 for x in stats])
    print(*stats)
    print(answer[count])
    print()