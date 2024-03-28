a = int(input())
b = int(input())
total,count = a+b,0
while total > 0:
    count += 1
    total = total//10
print(count)