n = int(input())
pos = list(map(int, input().split()))
pos.sort()
result = 0
if len(pos)%2 ==0:
    result = pos[int(len(pos)/2) -1]
else:
    result = pos[len(pos)//2]
print(result)