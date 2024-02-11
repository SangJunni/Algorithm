n = input()
if n.count('7') == 0 and int(n) % 7 != 0:
    print(0)
elif n.count('7') == 0 and int(n)% 7 == 0:
    print(1)
elif n.count('7') != 0 and int(n) % 7 != 0:
    print(2)
elif n.count('7') != 0 and int(n) % 7 == 0:
    print(3)