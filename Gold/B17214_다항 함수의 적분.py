poly = input()
if "+" in poly:
    a, b = map(int,poly.split('x+'))
    if a/2 != 1 and b!=1 and b!=0:
        print('%dxx+%dx+W' %(a/2, b))
    elif a/2 == 1 and b!=1 and b!=0:
        print('xx+%dx+W' %(b))
    elif a/2 == 1 and b==0:
        print('xx+W')
    elif a/2 != 1 and b==1:
        print('%dxx+x+W' %(a/2))
    elif a/2 != 1 and b==0:
        print('%dxx+W' %(a/2))
    else:
        print('xx+x+W')
elif "-" in poly:
    a, b = map(int,poly.split('x-'))
    if a / 2 != 1 and b != 1 and b != 0:
        print('%dxx+%dx+W' % (a / 2, b))
    elif a / 2 == 1 and b != 1 and b != 0:
        print('xx+%dx+W' % (b))
    elif a / 2 == 1 and b == 0:
        print('xx+W')
    elif a / 2 != 1 and b == 1:
        print('%dxx+x+W' % (a / 2))
    elif a / 2 != 1 and b == 0:
        print('%dxx+W' % (a / 2))
    else:
        print('xx+x+W')
elif "x" in poly:
    a = int(poly[:-1])
    if a / 2 == 1 :
        print('xx+W')
    else:
        print('%dxx+W' %(a/2))
else:
    poly = int(poly)
    if poly!=1 and poly!=0:
        print("%dx+W" %(poly))
    elif poly == 0:
        print('W')
    else:
        print("x+W")