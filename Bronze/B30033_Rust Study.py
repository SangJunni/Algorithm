n = int(input())
goal = list(map(int, input().split()))
real = list(map(int, input().split()))
count = 0
for i in range(n):
    if goal[i] <= real[i]:
        count += 1
print(count)