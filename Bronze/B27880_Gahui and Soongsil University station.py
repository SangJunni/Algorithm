result = 0
table = {'Es': 21, 'Stair': 17}
for _ in range(4):
    step, count = input().split()
    result += table[step]*int(count)
print(result)