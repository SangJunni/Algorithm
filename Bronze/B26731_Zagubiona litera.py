alphabet_set = set(chr(i) for i in range(ord('A'), ord('Z')+1))
line = input()
for l in line:
    alphabet_set.remove(l)
print(*alphabet_set)