n = int(input())
line = [list(map(int, input().split())) for _ in range(n)]
#print(line)
line.sort(key = lambda x: x[0])
#print(line)
dest = [0]*501
for s, d in line:
    dest[d] = max(dest[:d])+ 1
    #print(dest)
print(n- max(dest))