n, k = map(int, input().split())
schedules = list(map(int, input().split()))
tabs = []
answer = 0
for i in range(k):
    if schedules[i] in tabs:
        continue
    if len(tabs) != n:
        tabs.append(schedules[i])
        continue
    lfu = 0
    temp = 0
    for tab in tabs:
        if tab not in schedules[i:]:
            temp = tab
            break
        elif schedules[i:].index(tab) > lfu:
            lfu = schedules[i:].index(tab)
            temp = tab
    tabs[tabs.index(temp)] = schedules[i]
    answer += 1
print(answer)
