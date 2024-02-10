scores = list(map(int, input().split()))
for i in range(1, min(scores)+1):
    if scores[0] % i == 0 and scores[1] % i == 0:
        gcd = i
print(gcd)
print(int(scores[0]*scores[1]/gcd))