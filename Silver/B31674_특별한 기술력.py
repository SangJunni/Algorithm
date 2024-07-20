MOD = 10 ** 9 + 7
# 입력 받기
n = int(input())
heights = list(map(int, input().split()))

# 결과 계산 및 출력
heights.sort(reverse=True)  # 내림차순 정렬
total_sum = 0

for height in heights:
    total_sum = (total_sum + total_sum + height) % MOD
print(total_sum)