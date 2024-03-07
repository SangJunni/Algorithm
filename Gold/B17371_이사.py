import sys


def distance(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2


n = int(input())
convini = []

for _ in range(n):
    convini.append(tuple(map(int, sys.stdin.readline().split())))

_min = 9876543210
_min_idx = -1

for i in range(n):
    _max = -1
    _m_idx = -1
    for j in range(n):
        d = distance(convini[i][0], convini[i][1], convini[j][0], convini[j][1])
        if _max < d:
            _max = d
            _m_idx = i
    if _max < _min:
        _min = _max
        _min_idx = _m_idx

print(convini[_min_idx][0], convini[_min_idx][1])