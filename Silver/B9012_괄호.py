iteration = int(input())
for i in range(iteration):
    n_list = input()
    value = 0
    check = 1
    for each_p in n_list:
        if value < 0 and check != 0:
            print('NO')
            check = 0
        elif each_p == '(':
            value = value + 1
        elif each_p == ')':
            value = value - 1
    if value == 0 and check != 0:
        print('YES')
    elif check != 0:
        print('NO')


