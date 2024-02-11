citations = [3, 0, 6, 1, 5]


# 프로그래머스 테스트 케이스만 통과(1개)
def h_index(citations):
    s_citations = sorted(citations)
    max_h = 0
    for i in range(len(citations)-1, 0, -1):
        if len(s_citations) - i >= s_citations[i]:
            max_h = s_citations[i]
            break
    answer = max_h
    return answer


# 프로그래머스 제출 성공
def solution(citations):
    coefficient = [0] * (max(citations)+1)
    for i in range(len(citations)):
        coefficient[citations[i]] += 1
    max_h = 0
    for i in range(len(coefficient)):
        if sum(coefficient[i:]) >= i:
            max_h = i
    return max_h


print(h_index(citations))
