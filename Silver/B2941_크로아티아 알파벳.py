croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
line = input()
count = 0
while len(line) != 0:
    for cr in croa:
        if line.startswith(cr):
            line = line[len(cr):]
            count += 1
            break
    else:
        line = line[1:]
        count += 1
print(count)
