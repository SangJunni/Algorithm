n, k = map(int,input().split())
data_list = []
remove_list= []
for i in range(1,n+1):
    data_list.append(i)
pos = -1
print('<', end='')
while data_list:
    pos = pos + k
    pos = pos % len(data_list)
    print(data_list[pos], end='')
    if len(data_list) > 1:
        print(',', end =' ')
    data_list.pop(pos)
    pos = pos - 1
print('>', end='')
