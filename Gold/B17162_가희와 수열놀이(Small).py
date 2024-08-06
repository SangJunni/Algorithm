q, mod = map(int, input().split())
stack = []
mod_stack = [[] for _ in range(mod)]
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        temp = query[1] % mod
        mod_stack[temp].append(len(stack))
        stack.append(temp)
    elif query[0] == 2 and stack:
        val = stack.pop()
        mod_stack[val].pop()
    elif query[0] == 3:
        min_count = len(stack)
        flag = True
        for s in mod_stack:
            if not s:
                print(-1)
                flag = False
                break
            min_count = min(s[-1], min_count)
        if flag:
            print(len(stack) - min_count)