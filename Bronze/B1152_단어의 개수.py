a = input()
b = []
b = a.split(' ')
c = len(b)
if(b[0] == ''):
    c = c-1
if(b[-1] == ''):
    c = c-1
print(c)