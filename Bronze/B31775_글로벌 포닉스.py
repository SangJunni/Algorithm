checker = ['k', 'l', 'p']
for _ in range(3):
    temp = input()
    if temp[0] in checker:
        checker.remove(temp[0])
if len(checker) == 0:
    print('GLOBAL')
else:
    print('PONIX')