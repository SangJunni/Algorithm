exp = input()
op, a, b = '', '', ''
for i in range(1,len(exp)):
    if exp[i] in ['+', '-', '/', '*']:
        op = exp[i]
        a = exp[:i]
        b = exp[i+1:]
        break
num_a, num_b = int(a, 8), int(b, 8)
if op == '+':
    result = (num_a + num_b)
elif op == '-':
    result = (num_a - num_b)
elif op == '*':
    result = (num_a * num_b)
else:
    if num_b == 0:
        print('invalid')
        exit()
    result = (num_a // num_b)

if result < 0:
    print('-', end='')
    print(oct(result)[3:])
else:
    print(oct(result)[2:])