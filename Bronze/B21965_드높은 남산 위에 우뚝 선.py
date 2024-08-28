n = int(input())
data = list(map(int, input().split()))
peak = max(data)
peak_idx = data.index(peak)
increase, decrease = data[:peak_idx+1], data[peak_idx:]
if len(increase) != len(set(increase)) or len(decrease) != len(set(decrease)) or increase != sorted(increase) or decrease != sorted(decrease, reverse=True):
    print('NO')
else:
    print('YES')