n = int(input())
data = []
for i in range(n):
    name, s1, s2, s3 = input().split()
    data.append((name, int(s1), int(s2), int(s3)))
data.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in range(n):
    print(data[i][0])