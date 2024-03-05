s = int(input())
cnt = 0
sum_i = 0
for i in range(1, s+1):
    sum_i += i
    cnt += 1
    if sum_i > s:
        break
cnt -= 1
if s == 1:
    print(1)
else:
    print(cnt)