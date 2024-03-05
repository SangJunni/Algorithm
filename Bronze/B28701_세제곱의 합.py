n = int(input())
one,two,three = 0,0,0
for i in range(1,n+1):
    one += i
    two += i
    three += i**3
print(one)
print(two**2)
print(three)