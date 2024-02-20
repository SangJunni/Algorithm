n = int(input())
levels = [250, 200, 140, 100, 60]
stats = [5, 4, 3, 2, 1]
characters = sorted([int(input()) for _ in range(n)], reverse=True)
print(characters)
result = [0, 0]
for idx, character in enumerate(characters):
    print(idx,character)
    if idx == 42:
        break
    for k in range(5):
        if levels[k] <= character:
            result[0] += character
            result[1] += stats[k]
            break
print(*result)