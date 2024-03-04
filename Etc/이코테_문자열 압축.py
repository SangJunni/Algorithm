def my_solution(s):
    answer = len(s)
    if answer == 1:
        return answer
    for i in range(1, int(len(s)/2) + 1):
        new_s = ''
        repeat = 0
        for j in range(0, len(s), i):
            if j == 0:
                comp = s[j:j + i]
                repeat += 1
            elif comp == s[j: j + i]:
                repeat += 1
            elif comp != s[j:j + i]:
                if repeat == 1:
                    new_s += comp
                elif repeat >= 2:
                    new_s = new_s + str(repeat) + comp
                if j+i > len(s):
                    new_s += s[j:]
                    break
                else:
                    comp = s[j:j + i]
                repeat = 1
            if (j+i) >= len(s):
                if repeat == 1:
                    new_s += s[j:]
                    break
                else:
                    new_s = new_s + str(repeat)+ comp
                    break
            #print(repeat)
            #print(new_s)
            #print(comp)
        #new_s += s[j -i:]
        #print(new_s)
        if len(new_s) < answer:
            answer = len(new_s)

    return answer


def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        compressed = ''
        prev = s[0:step]
        count = 1
        for i in range(step, len(s), step):
            if prev == s[i:i + step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[i: i + step]
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
        print(compressed)
    return answer


# s = 'aabbaccc'
# s = 'ababcdcdababcdcd'
# s = 'abcabcdede'
# s = 'abcabcabcabcdededededede'
s = 'xababcdcdababcdcd'
print(s[15:20])
print(solution(s))