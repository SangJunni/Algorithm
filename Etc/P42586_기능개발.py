from collections import deque


def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        count = 0
        print(progresses)
        for i in range(len(progresses)):
            if progresses[i] >= 100:
                progresses.popleft()
                speeds.popleft()
                count += 1
            else:
                break
        if count > 0:
            answer.append(count)

    return answer

result = solution([93,30,55], [1,30,5])
print(result)