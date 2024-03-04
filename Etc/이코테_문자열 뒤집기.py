data = list(map(int, input()))
set0 = 0
set1 = 0
#최소 횟수를 구하기 위해서는 같은 숫자끼리만 flip을 진앻해야 함
for i in range(len(data)-1):
    if data[i] == 0 and data[i] != data[i+1]:
        set0 += 1
    elif data[i] == 1 and data[i] != data[i+1]: 
        set1 += 1
print(min(set0, set1))
