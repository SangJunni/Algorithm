n, k = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1 = sorted(arr1, reverse=True)
arr2 = sorted(arr2)

i = 1
while i <= k:
    if arr1[n-i] < arr2[n-i]:
        arr1[n-i], arr2[n-i] = arr2[n-i], arr1[n-i]
        i += 1
    else:
        break
print(sum(arr1))

