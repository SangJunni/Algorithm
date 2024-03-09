n = int(input())
seats = input()
seats = seats.replace('LL','R')
print(min(len(seats)+1, n))