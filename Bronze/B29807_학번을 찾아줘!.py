n = int(input())
scores = list(map(int,input().split())) + [0]*(5-n)
id = 0
if scores[0] > scores[2]:
    id += (scores[0] - scores[2]) *508
else:
    id += (scores[2] - scores[0]) *108
if scores[1] > scores[3]:
    id += (scores[1] - scores[3]) *212
else:
    id += (scores[3] - scores[1]) *305
id += scores[4] * 707
print(id*4763)