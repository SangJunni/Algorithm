n = int(input())
for i in range(n):
    m, data = map(str, input().split())
    for j in range(len(data)):
        print(data[j]*int(m), end='')
    print()