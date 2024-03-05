n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
people = 0
for i in a:
    temp = i -b
    if temp > 0:
        people += temp//c
        if temp % c != 0:
            people += 1
    people += 1
print(people)