socks = input()
result = [0,0]
for sock in socks:
    if sock == 'B':
        result[0] += 1
    else:
        result[1] += 1
print(result[0]//2 + result[1]//2)