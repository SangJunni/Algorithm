from math import floor
N, K, C, R = map(int, input().split())
base = [0] + list(map(int, input().split()))
s = [0] + list(map(int, input().split()))
p = [0] + list(map(int, input().split()))
skill = [0]*(K+1)
combo = 0
stardust = 0
fatigue = 0
for _ in range(N):
    current = int(input())
    if current == 0:
        combo = 0
        fatigue = max(fatigue - R, 0)
        continue
    stardust += base[current]*(100+combo*C)*(100+s[current]*skill[current])//10000
    skill[current] += 1
    combo += 1
    fatigue += p[current]
    if fatigue > 100:
        print(-1)
        break
else:
    print(stardust)