a = int(input())
b = int(input())
c = int(input())
total = str(a*b*c)
for i in range(10):
    value = total.count(str(i))
    print(value)