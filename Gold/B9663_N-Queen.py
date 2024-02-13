#9663
import sys
sys.setrecursionlimit(10**4)
n = int(input())
def nqueen(x, num, position):
    if x == num:
        return 1
    count = 0
    for y in range(num):
        if possible(x, y, num, position):
            position[x]= y
            count += nqueen(x+1, num, position)
    return count
def possible(x, y, num, position):
    for i in range(x):
        if y == position[i] or (x - i) == abs(y - position[i]):
            return False
    return True

position = [0]*n
answer = nqueen(0, n, position)
print(answer)