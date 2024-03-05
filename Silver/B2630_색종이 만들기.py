import sys
sys.setrecursionlimit(10**6)
n = int(input())
data = []
white = 0
blue = 0


def checking(data):
    global white
    global blue
    max_sum = len(data)**2
    if len(data) == 0:
        return False
    if sum([x.count(1) for x in data]) == max_sum:
        blue += 1
        return False
    elif sum([x.count(0) for x in data]) == max_sum:
        white += 1
        return False
    else:
        checking([x[:len(data)//2] for x in data[:len(data)//2]])
        checking([x[len(data)//2: len(data)] for x in data[:len(data)//2]])
        checking([x[:len(data)//2] for x in data[len(data)//2: len(data)]])
        checking([x[len(data)//2:len(data)] for x in data[len(data)//2: len(data)]])


for i in range(n):
    data.append(list(map(int, input().split())))
checking(data)
print(white)
print(blue)

