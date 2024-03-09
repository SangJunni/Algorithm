from decimal import Decimal
n, least = map(float, input().split())
n = int(n)
convert = {'F': 0.00,'D0': 1.00,'D+': 1.50,'C0': 2.00,'C+': 2.50,'B0': 3.00,'B+': 3.50,'A0': 4.00,'A+': 4.50}
total, score = 0,0
for _ in range(n-1):
    num, result = input().split()
    total += int(num)
    score += int(num)*Decimal(str(convert[result]))
last = int(input())
total += last
for key in convert:
    #print((score + last*Decimal(str(convert[key])))/total)
    calc = round((score + last*Decimal(str(convert[key])))/total, 3)
    calc = int(calc*100)/100
    #print(calc)
    if calc > least:
        print(key)
        break
else:
    print("impossible")