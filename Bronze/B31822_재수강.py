fail = input()
n = int(input())
total = 0
for _ in range(n):
    temp = input()
    if fail[:5] == temp[:5]:
        total += 1
print(total)