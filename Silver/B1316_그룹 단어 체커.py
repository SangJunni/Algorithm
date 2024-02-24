n = int(input())
result = 0
for _ in range(n):
    word = list(input())
    record = [word[0]]
    prev = word[0]
    flag = 0
    for w in word[1:]:
        if prev != w and w in record:
            flag = 1
            break
        elif prev != w:
            record.append(w)
            prev = w
    if flag == 0:
        result += 1
print(result)