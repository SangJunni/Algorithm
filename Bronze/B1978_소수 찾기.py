n = int(input())
data = list(map(int, input().split()))
remove_list = [1]
data = [x for x in data if x not in remove_list]
#print(data)
prime_count = len(data)
for d in data:
    for i in range(2, int(d**0.5)+1):
        if d % i == 0:
            prime_count -= 1
            break
print(prime_count)


