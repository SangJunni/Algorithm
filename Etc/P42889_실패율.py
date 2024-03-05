def solution(N, stages):
    answer = []
    stages.sort()
    coefficient = [0]*(N+2)
    fallacy_list = []
    sort_fallacy = []
    for i in range(len(stages)):
        coefficient[stages[i]] +=1
    for i in range(N):
        fallacy = coefficient[i+1]/sum(coefficient[i+1:])
        fallacy_list.append((i+1, fallacy))
    fallacy_list.sort(key=lambda x: (-x[1], x[0]))
    for i in range(len(fallacy_list)):
        sort_fallacy.append(fallacy_list[i][0])
    return sort_fallacy

#런타임 발생 -> 반복문 줄이기
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
result = solution(N, stages)
print(result)