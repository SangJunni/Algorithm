t = int(input())
n = int(input())
total = sum(list(map(int, input().split())))
if t <= total:
    print("Padaeng_i Happy")
else:
    print("Padaeng_i Cry")
