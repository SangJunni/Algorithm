a, b = map(int, input().split())
acre = 4840*5
print(a*b//acre if a*b%acre == 0 else a*b//acre + 1)