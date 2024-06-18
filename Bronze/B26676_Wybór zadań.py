checker = {'1A': 0, '1B': 0, '1C': 0, '2A': 0, '2B': 0,
           '2C': 0, '3A': 0, '3B': 0, '3C': 0, '4A': 0,
           '4B': 0, '4C': 0, '5A': 0, '5B': 0, '5C': 0}
n = int(input())
info = list(input().split())
for i in info:
    checker[i] += 1
for key in checker:
    if key in ['5A', '5B', '5C']:
        if checker[key] < 2:
            print('NIE')
            break
    else:
        if checker[key] < 1:
            print('NIE')
            break
else:
    print('TAK')
