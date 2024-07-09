m, n, a = map(int, input().split())
passengers = list(map(int, input().split()))
if a >= 1000:
    print('Impossible')
else:
    print((m + sum(passengers))*a/(1000-a))