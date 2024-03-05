id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
#report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 2
report_split =[]
report = list(set(report))
report_num = id_list.copy()
answer = 0
for i in range(len(id_list)):
    report_num[i] = 0

for component in report:
    reporter, reportee = component.split()
    report_num[id_list.index(reportee)] += 1
    print(report_num)
for i in range(len(id_list)):
    if(report_num[i]-k>=0):
        answer += report_num[i]
print(answer)

def solution(id_list, report, k):
    report_split =[[]]
    for i in range(len(report)):
        report_split = report.split()
    answer = []
    return answer