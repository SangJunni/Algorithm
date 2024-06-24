a, b = input().split()
length = len(a)
a, b = int(a), int(b)
answer = 0
for i in range(a, b):
    register = set()
    for l in range(1, length):
        temp = int(str(i % 10**l) + str(i // 10**l))
        if i < temp <= b and temp not in register:
            register.add(temp)
            answer += 1
print(answer)