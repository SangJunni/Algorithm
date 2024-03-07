n = int(input())
check = 0
for _ in range(3):
    temp = list(map(int,input().split()))
    if 7 in temp:
        check += 1
if check == 3:
    print(777)
else:
    print(0)