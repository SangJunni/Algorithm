line = input()
one = line.replace('0', ' ')
one = [x for x in one.split(' ') if x != '']
two = line.replace('1', ' ')
two = [x for x in two.split(' ') if x != '']
print(min(len(one), len(two)))