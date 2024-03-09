keypad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'
l_pos = [4,0]
r_pos = [4,2]
answer = ''
for number in numbers:
    if(number in [1, 4, 7]):
        answer += 'L'
        for i in range(len(keypad)):
            if number in keypad[i]:
                j = keypad[i].index(number)
                l_pos[0]= i
                l_pos[1]= j
    elif(number in [3, 6, 9]):
        answer += 'R'
        for i in range(len(keypad)):
            if number in keypad[i]:
                j = keypad[i].index(number)
                r_pos[0] = i
                r_pos[1] = j
    else:
        target_pos = [0, 0]
        for i in range(len(keypad)):
            if number in keypad[i]:
                j = keypad[i].index(number)
                target_pos[0] = i
                target_pos[1] = j
        left_length = abs(l_pos[0]-target_pos[0]) + abs(l_pos[1] - target_pos[1])
        right_length = abs(r_pos[0] - target_pos[0]) + abs(r_pos[1] - target_pos[1])
        if left_length < right_length:
            answer += 'L'
            l_pos[0] = target_pos[0]
            l_pos[1] = target_pos[1]
        elif left_length > right_length:
            answer += 'R'
            r_pos[0] = target_pos[0]
            r_pos[1] = target_pos[1]
        else:
            if hand == 'right':
                answer += 'R'
                r_pos[0] = target_pos[0]
                r_pos[1] = target_pos[1]
            else:
                answer += 'L'
                l_pos[0] = target_pos[0]
                l_pos[1] = target_pos[1]
print(answer)
