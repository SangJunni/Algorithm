from math import factorial
n = int(input())
result = str(factorial(n))
count = 0
for r in result[::-1]:
    if int(r) != 0:
        break
    else:
        count += 1
print(count)