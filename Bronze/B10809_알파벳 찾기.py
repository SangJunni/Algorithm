data = str(input())
pos = [-1]*26
for idx, d in enumerate(data):
    if pos[ord(d)-ord('a')] == -1:
        pos[ord(d)-ord('a')] = idx
for val in pos:
    print(val, end=' ')
print()