from collections import deque
n = int(input())
data = []
data = deque(data)
for i in range(1, n+1):
    data.append(i)
while len(data) != 1:
    data.popleft()
    temp = data[0]
    data.popleft()
    data.append(temp)
print(data[0])
#일반 리스트로 코드 구현 시 시간 초과 발생 이를 해결하기 위해서는 아래의 내장 함수를 사용해야함.
#from collections import deque ->리스트 대비 처리속도가 더 빠름