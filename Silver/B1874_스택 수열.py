n = int(input())
data = []
stack = []
answer = []
for _ in range(n):
    data.append(int(input()))
data = data[::-1]

for i in range(1, n + 1):
    stack.append(i)
    answer.append('+')
    while stack[-1] == data[-1]:
        answer.append('-')
        stack.pop()
        data.pop()
        if len(stack) == 0:
            break
if len(data) != 0:
    print('NO')
else:
    for a in answer:
        print(a)
