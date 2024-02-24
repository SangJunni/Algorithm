#파이썬이라서 값 범위에 대한 고려 필요X
# https://jason9319.tistory.com/113
n = int(input())
sequence = list(map(int, input().split()))
sub = [sequence[0]]
pos = 0
for i in range(1, n):
    if sub[pos] < sequence[i]:
        sub.append(sequence[i])
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
    #print(sub)
    #print(pos)
print(pos + 1)
