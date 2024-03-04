def binary_sort(data, target, start, end):
    if start > end:
        return None
    mid = (start + end)//2
    if data[mid] == target:
        return mid
    elif data[mid] > target:
        return binary_sort(data, target, start, mid-1)
    else:
        return binary_sort(data, target, mid+1, end)


N = int(input())
comp_list = list(map(int, input().split()))
M = int(input())
wish_list = list(map(int, input().split()))

comp_list.sort()
wish_list.sort()
result = 0
for i in range(M):
    result = binary_sort(comp_list, wish_list[i], 0, N-1)
    if result == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')

