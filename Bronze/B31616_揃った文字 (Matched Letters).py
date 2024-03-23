n = int(input())
word = list(input())
word = list(set(word))
if len(word) == 1:
    print('Yes')
else:
    print('No')