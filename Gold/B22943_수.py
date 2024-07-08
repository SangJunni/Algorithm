from itertools import permutations
k, m = map(int, input().split())
count = 0
max_val = 98765 // 10**(5-k)
status = [0]*(max_val + 1)
for cur in range(2,max_val + 1):
    if status[cur] == 0:
        status[cur] = 2
        multiple = 2
        while cur*multiple <= max_val:
            status[cur*multiple] = 1
            multiple += 1

for p in permutations([str(x) for x in range(10)], k):
    if p[0] == '0':
        continue
    current = int(''.join(p))
    for i in range(2, current // 2):
        if status[i] == 2 and status[current - i] == 2:
            temp = current
            while temp % m == 0:
                temp //= m
            for j in range(2, int(temp ** 0.5)+1):
                if temp % j == 0 and status[j] == 2 and status[temp // j] == 2:
                    count += 1
                    break
            break
print(count)