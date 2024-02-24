data = input()
while data !='.':
    temp = list(data)
    stack = []
    for t in temp:
        if t == '[' or t == '(':
            stack.append(t)
            continue
        elif t == ']':
            if len(stack) == 0:
                stack.append(t)
                break
            if stack[-1] == '[':
                stack.pop()
                continue
            else:
                break
        elif t == ')':
            if len(stack) == 0:
                stack.append(t)
                break
            if stack[-1] == '(':
                stack.pop()
                continue
            else:
                break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')
    data = input()