from datetime import *
today = list(map(int, input().split()))
dday = list(map(int, input().split()))
if today[0] + 1000 < dday[0] or (today[0] + 1000 == dday[0] and (today[1], today[2]) <= (dday[1], dday[2])):
    print('gg')
else:
    today = date(*today)
    dday = date(*dday)
    print(f'D-{dday.toordinal() - today.toordinal()}')

