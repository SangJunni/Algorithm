data = list(map(str, input()))
data.sort()
total = 0
result = ''
for x in data:
    if x >= '0' and x<='9':
        total += int(x)
    else:
        result +=x
result += str(total)
print(result)

#K1KA5CB7
#AJKDLSI412K4JSJ9D