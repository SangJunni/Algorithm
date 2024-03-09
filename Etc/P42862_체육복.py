n = 5
lost = [2, 4]
reserve = [3]
students = []
for i in range(n):
    students.append(1)
for i in lost:
    students[i - 1] = students[i - 1] - 1
for i in reserve:
    students[i - 1] = students[i - 1] + 1
for i in range(n):
    print(students[i])
    if students[i] == 0 and i == 0 and students[i + 1] == 2:
        students[i] = 1
        students[i + 1] = 1
    elif students[i] == 0 and i == (n - 1) and students[i - 1] == 2:
        students[i] = 1
        students[i - 1] = 1
    elif students[i] == 0 and i != 0 and i != (n - 1):
        if students[i - 1] == 2:
            students[i] = 1
            students[i - 1] = 1
            print("왼쪽에서 빌림")
            print(students)
        elif students[i + 1] == 2:
            students[i] = 1
            students[i + 1] = 1
print(students)
count = 0
for i in range(n):
    if students[i] >= 1:
        count = count + 1
answer = count
print(answer)
