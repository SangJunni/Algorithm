n= int(input())
data = list(map(int, input().split()))
data.sort()
data2 = data.copy()
###### 내가 생각한 해결방안
# 가장 공포도가 큰 사람들부터 그룹화하여 줄여나가는 방식
# 예상되는 문제점: 한명만 공포도가 매우 큰 경우 그룹 수가 최소화 됨 --> 문제점
team = 0
fear = max(data)
while True:
    if len(data) < fear:
        break
    if len(data) == fear:
        team += 1
        break
    if len(data) > fear:
        data = data[:len(data) - fear]
        fear = data[-1]
        team += 1
print(team)
###### 책에서 제시하는 방법
#가장 공포도를 작은 사람부터 그룹화 --> 가장 많은 그룹을 생성할 수 있음
team = 0
total = 0
for x in data2:
    total += 1
    if total >= x:
        team += 1
        total = 0
print(team)
