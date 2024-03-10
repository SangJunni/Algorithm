n = int(input())
for _ in range(n):
    line = input()
    if line[-1] != '.':
        print(line + '.')
    else:
        print(line)