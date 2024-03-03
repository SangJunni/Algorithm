before_divide = 0
divider = 0
score2num = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
for _ in range(20):
    subject, credit, score = input().split()
    if score == 'P':
        continue
    before_divide += float(credit) * score2num[score]
    divider += float(credit)
print(f"{before_divide/divider: .6f}")