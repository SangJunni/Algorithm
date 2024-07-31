word = input()
dial = [chr(x) for x in range(65, 91)]
prev = 'A'
move = 0
for w in word:
    gap = abs(ord(prev) - ord(w))
    move += min(gap,26-gap)
    prev = w
print(move)