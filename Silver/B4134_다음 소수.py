t = int(input())
for _ in range(t):
    n = int(input())
    while True:
        if n <= 1:
            print(2)
            break
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                is_prime = 0
                break
        else:
            is_prime = 1
        if is_prime:
            print(n)
            break
        else:
            n += 1