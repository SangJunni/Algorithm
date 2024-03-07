def binary_search(data, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if data[mid] == target:
        return mid
    elif data[mid] > target:
        return binary_search(data, target, start, mid -1)
    else:
        return binary_search(data, target, mid +1, end)


def binary_search2(data, target, start, end):
    while start <= end:
        mid = (start + end)//2
        if data[mid] == target:
            return mid
        elif data[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None


n, target = map(int, input().split())
data = list(map(int, input().split()))
result = binary_search(data, target, 0, n-1)
result2 = binary_search(data, target, 0, n-1)
if result == None:
    print("존재 x")
else:
    print(result + 1)
if result2 == None:
    print("존재 x")
else:
    print(result2 + 1)