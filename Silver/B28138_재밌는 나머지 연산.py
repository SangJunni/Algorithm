n, r = map(int, input().split())
total = 0
def divisor(n, r):
    possible = []
    x = n-r
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            possible.append(i)
            if i**2 != x:
                possible.append(x//i)
    return sum([x if x > r else 0 for x in possible])
print(divisor(n, r))