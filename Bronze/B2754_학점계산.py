n = list(input())
score = {'F': 0.0, 'D': 1.0, 'C':2.0, 'B': 3.0, 'A':4.0}
if len(n) == 1:
    print(score[n[0]])
else:
    if n[1] == '+':
        result = float(score[n[0]] + 0.3)
        print(result)
    elif n[1] == '-':
        result = float(score[n[0]] - 0.3)
        print(result)
    else:
        print(score[n[0]])