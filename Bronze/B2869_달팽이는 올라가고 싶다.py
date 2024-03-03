a,b,v = map(int, input().split())
answer = (v-b)/(a-b)
print(int(answer) if answer == int(answer) else int(answer)+1)