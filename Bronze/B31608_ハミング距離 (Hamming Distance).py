n = int(input())
a = input()
b = input()
result = 0
for x,y in zip(a,b):
    if x != y:
        result += 1
print(result)