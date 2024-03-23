line = list(input())
result = []
for idx, a in enumerate(line):
    if idx == 0:
        result.append(a)
    else:
        if line[idx-1] != a:
            result.append(a)
print(''.join(result))