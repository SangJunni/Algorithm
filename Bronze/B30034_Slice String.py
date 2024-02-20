alphabet = []
num = []
n = int(input())
alphabet = set(list(input().split()))
n = int(input())
num = set(list(input().split()))
n = int(input())
merge = list(input().split())
for m in merge:
    if m in alphabet:
        alphabet.remove(m)
    if m in num:
        num.remove(m)
n = int(input())
line = input()
erase = alphabet | num
for e in erase:
    line = line.replace(e, ' ')
result = list(line.split())
for r in result:
    print(r)