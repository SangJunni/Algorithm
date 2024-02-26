a,b = map(int, input().split())
zero,one = 0,0
for _ in range(a):
    line = list(input())
    zero += line.count('0')
    one += line.count('1')
print(min(zero,one))