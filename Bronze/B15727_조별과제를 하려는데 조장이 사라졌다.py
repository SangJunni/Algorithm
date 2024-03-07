n = int(input())
a,b = divmod(n, 5)
if b != 0:
    total = a+1
else:
    total = a
print(total)