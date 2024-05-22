n = int(input())
line = input()
odd, even = 0, 0
for l in line:
    if int(l) % 2 == 0:
        even += 1
    else:
        odd += 1
if odd > even:
    print(1)
elif even > odd:
    print(0)
else:
    print(-1)
