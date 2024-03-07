from datetime import datetime
def is_need_check_next_year(submission_month, deadline_month, submission_year):
    is_need_check = False
    deadline_year = submission_year
    if submission_month == 12 and deadline_month == 1:
        is_need_check = True
        deadline_year += 1
    elif submission_month == 1 and deadline_month == 12:
        is_need_check = True
        deadline_year -= 1

    return is_need_check, deadline_year


def is_leap_year(year):
    is_leap = False

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        is_leap = True

    return is_leap


def datetime_to_string(date):
    return '{dt.month}/{dt.day}/{dt.year}'.format(dt=date)


def is_grade_homework(term, submission_day, deadline_day):
    day_status = "SAME DAY"
    if term < -7 or term > 7:
        day_status = "OUT OF RANGE"
    elif 0 < term < 8:
        day_status = f"{datetime_to_string(deadline_day)} IS {term} {'DAYS' if term > 1 else 'DAY'} AFTER"
    elif -8 < term < 0:
        day_status = f"{datetime_to_string(deadline_day)} IS {abs(term)} {'DAYS' if abs(term) > 1 else 'DAY'} PRIOR"

    return day_status


def calculate_date_term(submission_month, submission_day, submission_year,
                        deadline_month, deadline_day):
    is_submission_year_leap = is_leap_year(submission_year)

    is_need_check, deadline_year = is_need_check_next_year(submission_month, deadline_month, submission_year)

    if not is_submission_year_leap:
        if deadline_month == 2 and deadline_day == 29:
            deadline_year = 2004

    submission_day = datetime(year=submission_year, month=submission_month, day=submission_day)
    deadline_day = datetime(year=deadline_year, month=deadline_month, day=deadline_day)

    term = (deadline_day - submission_day).days

    return term, submission_day, deadline_day


def os_homework_submission_date(submission_date, deadline):
    submission_month, submission_day, submission_year = map(int, submission_date.split("/"))
    deadline_month, deadline_day = map(int, deadline.split("/"))

    term, submission_day, deadline_day = calculate_date_term(submission_month, submission_day, submission_year,
                                                             deadline_month, deadline_day)

    return is_grade_homework(term, submission_day, deadline_day)


if __name__ == "__main__":
    for _ in range(int(input())):
        submission_date, deadline = input().split()
        print(os_homework_submission_date(submission_date, deadline))