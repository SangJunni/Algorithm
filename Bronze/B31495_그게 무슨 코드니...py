line = input()
if line[0] == '"' and line[-1] == '"' and len(line) >=3:
    print(line[1:-1])
else:
    print('CE')