n = int(input())
sequence = []
for _ in range(n):
    sequence.append(list(map(int, input().split())))
sequence.sort(key=lambda x: x[0])
sub = [sequence[0]]
record = [0] * n
record[0] = 1
pos = 0
for i in range(1, n):
    if sub[pos][1] < sequence[i][1]:
        sub.append(sequence[i])
        record[i] = len(sub)
        pos += 1
    elif sub[pos][1] > sequence[i][1]:
        start = 0
        end = pos
        flag = 0
        while start <= end:
            mid = (start + end)//2
            if sub[mid][1] > sequence[i][1]:
                end = mid - 1
            elif sub[mid][1] < sequence[i][1]:
                start = mid + 1
            else:
                flag = 1
                break
        if flag == 0:
            sub[start] = sequence[i][:]
            record[i] = start + 1
    #print(sub)
    #print(pos)
print(n-(pos + 1))
find_dp = pos + 1
ans = []
for i in range(len(record) - 1, -1, -1):
    if record[i] == find_dp:
        ans.append(sequence[i][0])
        find_dp -= 1

    if find_dp < 1:
        break
true = [sequence[x][0] if sequence[x][0] not in ans else -1 for x in range(n)]
for t in true:
    if t != -1:
        print(t)