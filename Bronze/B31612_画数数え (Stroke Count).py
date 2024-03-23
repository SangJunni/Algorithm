n = int(input())
word = input()
result = 0
for w in word:
    if w in ['i','j']:
        result += 2
    else:
        result += 1
print(result)