n = int(input())
for _ in range(n):
    temp = int(input())
    if temp % 2 == 0:
        print(f'{temp} is even')
    else:
        print(f'{temp} is odd')