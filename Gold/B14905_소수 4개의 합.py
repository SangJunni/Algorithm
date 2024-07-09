while True:
    try:
        n = int(input())
        if n < 8:
            print('Impossible.')
        else:
            if n % 2 == 0:
                result = [2, 2]
                n -= 4
            else:
                result = [2, 3]
                n -= 5
            for i in range(2, n//2+1):
                p1, p2 = True, True
                for j in range(2, int(i**0.5)+1):
                    if i % j == 0:
                        p1 = False
                        break
                for j in range(2, int((n-i)**0.5)+1):
                    if (n-i) % j == 0:
                        p2 = False
                        break
                if p1 and p2:
                    result = result + [i, n-i]
                    break
            print(*result)
    except:
        break