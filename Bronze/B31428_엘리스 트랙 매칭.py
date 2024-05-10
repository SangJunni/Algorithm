n = int(input())
line = list(input().split())
status = {'C':0,'S':0,'I':0,'A':0}
for l in line:
    status[l] += 1
a = input()
print(status[a])