n, prize = map(int, input().split())
solved = []
total = 0
for _ in range(n):
    temp = int(input())
    solved.append(temp)
    total += temp
for i in range(n):
    print(prize//total*solved[i])