n, h, w = map(int, input().split())
answer = ['?']*n
for _ in range(h):
    temp = input()
    for i in range(0,len(temp), w):
        for j in range(w):
            if temp[i+j] != '?':
                answer[i//w] = temp[i+j]
print(''.join(answer))