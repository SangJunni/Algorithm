def solution(priorities, location):
    answer = 0
    while True:
        current = priorities.pop(0)
        if current >= max(priorities):
            if location == 0:
                answer+=1
                break;
            else:
                location -=1
                answer +=1
        else:
            location -=1
            priorities.append(current)
            if location < 0:
                location = len(priorities) - 1
        print(priorities)
        print(location)
    return answer

priorities = [1,1,9,1,1,1]
location = 0
result = solution(priorities, location)
print(result)