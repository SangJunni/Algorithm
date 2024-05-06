line = input()
dict = {'A': 0, 'B': 0}
for l in line:
    dict[l] += 1
print(f"{dict['A']} : {dict['B']}")