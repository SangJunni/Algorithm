n = int(input())
table = [0]*1_000_002
for _ in range(n):
    start, end = map(int, input().split())
    table[start] += 1
    table[end+1] -= 1
for i in range(1, 1_000_001):
    table[i] += table[i-1]
q = int(input())
when = list(map(int, input().split()))
for wh in when:
    print(table[wh])