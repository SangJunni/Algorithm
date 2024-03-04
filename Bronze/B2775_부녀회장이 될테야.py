t = int(input())
apartment = [[x for x in range(1,15)]] + [[1] +[0]*13 for _ in range(14)]
for i in range(1,15):
    for j in range(1,14):
        apartment[i][j] = apartment[i-1][j] + apartment[i][j-1]
for _ in range(t):
    floor = int(input())
    room = int(input())
    print(apartment[floor][room-1])
