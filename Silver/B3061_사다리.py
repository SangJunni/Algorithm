T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    swap = 0
    for i in range(N):
        for j in range(N-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
                swap += 1
    print(swap)