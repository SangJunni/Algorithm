operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
def solution(operations):
    answer = []
    queue = []
    for i in range(len(operations)):
        command, num = operations[i].split(' ')
        if command == 'I':
            queue.append(int(num))
        elif command == 'D':
            if int(num) == -1 and len(queue) != 0:
                queue.remove(min(queue))
            elif len(queue) != 0:
                queue.remove(max(queue))
    if len(queue)!=0:
        answer.append(max(queue))
        answer.append(min(queue))
    else:
        answer = [0,0]
    return answer
answer = solution(operations)
print(answer)
