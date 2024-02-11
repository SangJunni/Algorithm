condition = list(map(int, input().split()))
trees = list(map(int, input().split()))
max_height = min(max(trees), 1000000000)
min_height = 0

def cal(mid):
    total = 0
    for i in trees:
        if i >= mid:
            total += i-mid
    return total

while max_height >= min_height:
    cut_height = int((max_height + min_height)/2)
    value = 0;
    total = cal(cut_height)
    if total >= condition[1]:
        min_height = cut_height + 1
    else:
        max_height = cut_height - 1
print(max_height)
