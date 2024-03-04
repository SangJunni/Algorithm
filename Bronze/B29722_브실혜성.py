# 입력
today = input().strip().split('-')
year, month, day = int(today[0]), int(today[1]), int(today[2])
N = int(input())

# 날짜 계산
new_day = (day + N - 1) % 30 + 1
new_month = month + (day + N - 1) // 30
new_year = year + new_month // 12
new_month %= 12
if new_month == 0:
    new_month = 12
    new_year -= 1

# 출력
print(f"{new_year:04d}-{new_month:02d}-{new_day:02d}")
