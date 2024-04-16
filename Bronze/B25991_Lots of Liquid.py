n = int(input())
chem = list(map(float,input().split()))
total = 0
for ch in chem:
    total += ch**3
print(total**(1/3))