from fractions import Fraction
#백준 2407번
n, m = map(int, input().split())
nom = 1
denom = 1
if n == m:
    result = 1
if n-m < n-(n-m):
    for i in range(1, n-m+1):
        nom *= (n-i + 1)
        denom *= i
    result = int(Fraction(nom, denom))
else:
    for i in range(1, m+1):
        nom *= (n - i + 1)
        denom *= i
    result = int(Fraction(nom, denom))
print(int(result))