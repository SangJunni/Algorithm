n = int(input())
sequence = list(map(int, input().split()))
sub = [sequence[0]]
record = [0] * n
record[0] = 1
pos = 0
for i in range(1, n):
    if sub[pos] < sequence[i]:
        sub.append(sequence[i])
        record[i] = len(sub)
        pos += 1
    elif sub[pos] > sequence[i]:
        start = 0
        end = pos
        flag = 0
        while start <= end:
            mid = (start + end)//2
            if sub[mid] > sequence[i]:
                end = mid - 1
            elif sub[mid] < sequence[i]:
                start = mid + 1
            else:
                flag = 1
                break
        if flag == 0:
            sub[start] = sequence[i]
            record[i] = start + 1
    #print(sub)
    #print(pos)
print(pos + 1)
find_dp = pos + 1
ans = []
for i in range(len(record) - 1, -1, -1):
    if record[i] == find_dp:
        ans.append(sequence[i])
        find_dp -= 1

    if find_dp < 1:
        break
print(*ans[::-1])