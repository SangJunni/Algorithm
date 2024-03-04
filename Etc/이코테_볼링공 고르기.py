n, m = map(int, input().split())
data = list(map(int, input().split()))
coefficient = [0]*(m+1)
total = n * (n-1) / 2
for i in range(len(data)):
    coefficient[data[i]] += 1
#print(coefficient)
#print(total)
for x in coefficient[1:]:
    if x > 1:
        total -= (x*(x-1)/2)
print(int(total))
#내가 생각한 방식 확률 개념이용: 전체 콤비네이션 중 같은 무게를 뽑는 모든 콤비네이션 제거
#책에서 제안하는 방법: A가 선택하는 무게를 늘려가면서 경우의 수 세기