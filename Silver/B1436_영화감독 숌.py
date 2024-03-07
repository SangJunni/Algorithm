n = int(input())
count = 0
check = 0
while count < n:
    if str(check).find('666') != -1:
        count += 1
    check += 1
print(check-1)