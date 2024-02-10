a = input()
b = []
b = a.split(' ')

if int(b[0]) > int(b[1]):
    print('>')
elif int(b[0]) < int(b[1]):
    print('<')
elif int(b[0]) == int(b[1]):
    print('==')