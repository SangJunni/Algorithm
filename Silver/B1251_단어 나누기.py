from itertools import combinations
word = input()
length = len(word)
result = []
for comb in combinations(range(1, length), 2):
    start, end = min(comb), max(comb)
    first, mid, end = word[:start][::-1], word[start:end][::-1], word[end:][::-1]
    result.append(first+mid+end)
result.sort()
print(result[0])