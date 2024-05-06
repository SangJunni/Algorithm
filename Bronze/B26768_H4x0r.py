s2n = {'a':'4','e':'3','i':'1','o':'0','s':'5'}
line = input()
for s in s2n:
    line = line.replace(s,s2n[s])
print(line)