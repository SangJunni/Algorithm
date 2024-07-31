from math import ceil
n = int(input())
shorts = list(map(int, input().split()))
t,p = map(int, input().split())
print(sum([ceil(x/t) for x in shorts]))
print(n//p,n%p)