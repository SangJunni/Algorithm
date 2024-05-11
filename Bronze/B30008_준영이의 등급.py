n,k = map(int, input().split())
cutlines = [4,11,23,40,60,77,89,96,100]
scores = list(map(int, input().split()))
result = []
for score in scores:
    percentage = score*100//n
    for idx, cut in enumerate(cutlines):
        if percentage <= cut:
            result.append(idx+1)
            break
print(*result)