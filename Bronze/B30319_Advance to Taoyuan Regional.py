from datetime import datetime, timedelta


def check_contest_date(contest_date):
    icpc_regional_date = datetime(2023, 10, 21)
    threshold_date = icpc_regional_date - timedelta(days=35)

    contest_date = datetime.strptime(contest_date, '%Y-%m-%d')

    if contest_date > threshold_date:
        return "TOO LATE"
    else:
        return "GOOD"


# 입력 받기
contest_date = input().strip()

# 결과 출력
print(check_contest_date(contest_date))