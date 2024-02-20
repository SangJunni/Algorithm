n = int(input())
data = list(input())
way = ['W', 'S', 'E', 'N']
key = [0, 0, 0, 0]
for d in data:
    key[way.index(d)] += 1
print(n - max(key))