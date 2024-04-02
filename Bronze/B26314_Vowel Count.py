n = int(input())
vowel = ['a','e', 'i', 'o', 'u']
for _ in range(n):
    word = input()
    v,nv = 0,0
    for w in word:
        if w in vowel:
            v += 1
        else:
            nv += 1
    print(word)
    if v > nv:
        print(1)
    else:
        print(0)