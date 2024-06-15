t = int(input())
k, m1, m2 = map(int, input().split())
answer = 0
for _ in range(t):
    line = list(map(int, input().split()))
    h = line[0]
    count = 0
    for l in line[2:]:
        if l * m1 < h or l*m2 > h * k:
            answer += 1
print(answer)
