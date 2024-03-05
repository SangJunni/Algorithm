while True:
    lines = sorted(list(map(int, input().split())))
    if sum(lines) == 0:
        break
    if lines[0] + lines[1] <= lines[2]:
        print('Invalid')
        continue
    lines = list(set(lines))
    if len(lines) == 3:
        print('Scalene')
    elif len(lines) == 2:
        print('Isosceles')
    else:
        print('Equilateral')