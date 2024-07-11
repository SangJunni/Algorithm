t = int(input())
for _ in range(t):
    n = int(input())
    permutation = list(map(int, input().split()))
    new_permutation = [0]
    for idx, p in enumerate(permutation):
        min_temp = min(n - p + 1, p)
        max_temp = max(n - p + 1, p)
        if min_temp >= new_permutation[idx]:
            new_permutation.append(min_temp)
        elif max_temp >= new_permutation[idx]:
            new_permutation.append(max_temp)
        else:
            print('NO')
            break
    else:
        print('YES')