n, m = map(int, input().split())
friend_list = [set() for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    friend_list[a].add(b)
    friend_list[b].add(a)

days = 0
new_friends_count = []
while True:
    total_connections = 0
    for i in range(1,n+1):
        total_connections += len(friend_list[i])
    if total_connections == n * (n-1):
        break
    new_friend = set()
    for i in range(1,n+1):
        for j in friend_list[i]:
            for k in friend_list[j]:
                if not i == k and k not in friend_list[i]:
                    if i < k:
                        new_friend.add((i, k))
                    else:
                        new_friend.add((k, i))

    for a,b in new_friend:
        friend_list[a].add(b)
        friend_list[b].add(a)
    days += 1
    new_friends_count.append(len(new_friend))

print(days)
for nfc in new_friends_count:
    print(nfc)