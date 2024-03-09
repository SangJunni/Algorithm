n = input()
length = len(n)
if n == n[0]*length:
    print(-1)
elif n == n[::-1]:
    print(length-1)
else:
    print(length)