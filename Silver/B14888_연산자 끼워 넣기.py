from itertools import permutations
n= int(input())
data = list(map(int, input().split()))
num_list = list(map(int, input().split()))
numerator = []
for i in range(4):
    for j in range(num_list[i]):
        if i == 0:
            numerator.append('+')
        elif i == 1:
            numerator.append('-')
        elif i == 2:
            numerator.append('*')
        else:
            numerator.append('/')
choices = list(set(permutations(numerator, len(numerator))))
result_list = []
for choice in choices:
    total = data[0]
    for pos in range(len(choice)):
        if choice[pos] == '+':
            total += data[pos + 1]
        elif choice[pos] == '-':
            total = total - data[pos + 1]
        elif choice[pos] == '*':
            total = total * data[pos + 1]
        else:
            if total < 0:
                total = -1 * (abs(total)//data[pos+1])
            else:
                total = total//data[pos + 1]
    result_list.append(int(total))
print(max(result_list))
print(min(result_list))