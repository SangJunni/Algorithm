a = list(str(input()))
b = list(str(input()))
left = []
for alphabet in b:
    if alphabet in a:
        a.remove(alphabet)
    else:
        left.append(b)

print(len(left))