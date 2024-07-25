n,x = map(int, input().split())
min_weights = list(map(int, input().split()))
gain_weights = list(map(int, input().split()))
weight = 0
for idx, g in enumerate(gain_weights):
    weight += g
    if weight < min_weights[idx]:
        print(-1)
        exit()
print((weight - min_weights[-1])//x)