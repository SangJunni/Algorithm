val = input()
if len(val) == 3:
    if val[1] == '0':
        print(int(val[:2]) + int(val[-1]))
    else:
        print(int(val[0]) + int(val[1:]))
elif len(val) == 4:
    print(int(val[:2]) + int(val[2:]))
else:
    print(int(val[0]) + int(val[1]))

