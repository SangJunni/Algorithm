def power(A, n):
    res = 1
    while n:
        if n % 2 != 0:
            res *= A
        A *= A
        n //= 2
    return res


def factorization(x):
    d = 2
    factorization = []
    while d <= x:
        if x % d == 0:
            factorization.append(d)
            x = x / d
        else:
            d = d + 1
    return factorization


while True:
    n = int(input())
    if n == 0:
        break
    primes = factorization(n)
    k = 1
    for p in set(primes):
        k *= power(p, (primes.count(p) - 1)) * (p - 1)
    if n == 1:
        print(0)
    else:
        print(k)