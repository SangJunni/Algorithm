nominator, denominator = map(int,input().split())
coefficient, constant = map(int, input().split())
x0 = int(input())

# 극한값 L
result_L = coefficient * x0 + constant
print(result_L)

# 표현 불가
if int(coefficient) == 0:
    print("0 0")
else:
    result1 = int(nominator)
    result2 = int(denominator) * abs(coefficient)
    print(result1, result2)
