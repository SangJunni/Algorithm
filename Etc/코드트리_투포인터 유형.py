n, a, b = map(int, input().split())
sequence = list(map(int, input().split()))

left = 0
right = 0
current_sum = 0
min_length = float('inf')

while right < n:
    current_sum += sequence[right]

    while current_sum >= a:
        if current_sum - sequence[left] >= a:
            current_sum -= sequence[left]
            left += 1
        else:
            break

    if a <= current_sum <= b:
        # 현재 구간 내의 합이 [a, b] 범위에 속하면 구간의 길이를 갱신
        min_length = min(min_length, right - left + 1)

    right += 1

# 결과 출력
if min_length == float('inf'):
    print(-1)
else:
    print(min_length)