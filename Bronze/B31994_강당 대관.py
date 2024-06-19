result = ['',0]
for _ in range(7):
    name, cnt = input().split()
    cnt = int(cnt)
    if cnt > result[1]:
        result = [name, cnt]
print(result[0])