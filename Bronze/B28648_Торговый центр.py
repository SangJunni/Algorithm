n = int(input())
cases = []
for _ in range(n):
    a,b= map(int, input().split())
    cases.append(a+b)
print(min(cases))