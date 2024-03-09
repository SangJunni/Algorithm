n = int(input())
fib_list = [[1, 0], [0, 1]]
for i in range(n):
    find = int(input())
    if find < len(fib_list):
        print(fib_list[find][0], end= ' ')
        print(fib_list[find][1])
    else:
        for j in range(len(fib_list), find+1):
            fib_list.append([fib_list[j-1][0] + fib_list[j-2][0], fib_list[j-1][1] + fib_list[j-2][1]])
        print(fib_list[find][0], end=' ')
        print(fib_list[find][1])
