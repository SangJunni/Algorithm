def func(L, N, K, stones):
    left, right = max_dist, L
    result = 0
    while left <= right:
        mid = (left + right) // 2
        now,pos,cnt = mid, 0, 0
        for i in range(N+1):
            if stones[i] - pos > now:
                cnt += 1
                now = mid
            now -= (stones[i] - pos)
            pos = stones[i]
        if cnt <= K:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    print(result)


L, N, K = map(int, input().split())
charger = list(map(int, input().split()))
max_dist = max(charger[0], L - charger[-1])
for i in range(1, N):
    max_dist = max(max_dist, charger[i] - charger[i - 1])
charger.append(L)  # 마지막 돌까지 포함
func(L, N, K, charger)