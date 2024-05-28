h = list(input())
a,b = 0,0
for i in range(0,len(h),2):
    player,score = h[i],int(h[i+1])
    if player == 'A':
        a += score
    else:
        b += score
if a > b:
    print('A')
else:
    print('B')