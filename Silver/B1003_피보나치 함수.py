def fib(n):
    global num0
    global num1
    if n == 0:
        num0 +=1
        return 1
    elif n ==1:
        num1 +=1
        return 1
    else:
        return fib(n-1) + fib(n-2)


n = int(input())
for i in range(n):
    value = int(input())
    num0 = 0
    num1 = 0
    fib(value)
    print(num0, end=' ')
    print(num1)
#런타임 초과
