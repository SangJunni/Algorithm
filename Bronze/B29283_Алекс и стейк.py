n = int(input())
result = 0
time = 30
for i in range(1,n+1):
    result += time
    if i % 5 == 0:
        time += 30
print(result)