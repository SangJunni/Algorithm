n = int(input())
data = [0]*(n+1)
sequence = [[x] for x in range(0, n+1)]
for i in range(2, n+1):
    data[i] = data[i-1] + 1
    sequence[i] = sequence[i] + sequence[i-1]
    if i % 3 == 0:
        if data[i] > data[i//3] + 1:
            data[i] = data[i//3] + 1
            sequence[i] = [i] + sequence[i//3]
    if i % 2 == 0:
        if data[i] > data[i // 2] + 1:
            data[i] = data[i // 2] + 1
            sequence[i] = [i] + sequence[i//2]
        #data[i] = min(data[i], data[i//2]+1)
print(data[n])
for s in sequence[n]:
    print(s, end=' ')
# 최적의 방법 미존재: 모든 경우를 구해야 함