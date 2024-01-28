mobis = ['M', 'O', 'B', 'I', 'S']
line = input()
count = 0
for m in mobis:
    if m in line:
        count += 1
if count == 5:
    print('YES')
else:
    print('NO')