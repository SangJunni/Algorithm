import bisect
n, m = map(int, input().split())
meteor = list(map(int, input().split()))
meteor.sort()
planets = []
planets_weight = {}
for _ in range(m):
    pos, weight = map(int, input().split())
    planets.append(pos)
    planets_weight[pos] = weight
planets.sort()
power = 0
for i in range(m):
    idx = bisect.bisect_left(meteor, planets[i])
    # 왼쪽 끝인 경우
    if idx == 0:
        dist = abs(meteor[0]- planets[i])
        power = max(power, dist*planets_weight[planets[i]])
    elif idx == n:
        dist = abs(meteor[-1] - planets[i])
        power = max(power, dist * planets_weight[planets[i]])
    else:
        dist = min(abs(meteor[idx] - planets[i]), abs(meteor[idx-1] - planets[i]))
        power = max(power, dist * planets_weight[planets[i]])
print(power)