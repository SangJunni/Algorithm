h,m,s = map(int, input().split())
time = int(input())
h += time//3600
time =time % 3600
m += time//60
time = time % 60
s += time
if s >= 60:
    m += s//60
    s = s%60
if m >= 60:
    h += m//60
    m= m%60
if h >= 24:
    h = h%24
print(h,m,s)