n = int(input())
data = []
for i in range(n):
    student = input().split()
    data.append((student[0], student[1]))
data = sorted(data, key= lambda z: z[1])

for student in data:
    print(student[0], end=' ')
