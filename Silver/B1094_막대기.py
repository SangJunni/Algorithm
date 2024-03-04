sticks = [64]
length = int(input())
while sum(sticks) > length:
    sticks.sort(reverse = True)
    short = sticks.pop()
    if short/2 + sum(sticks) >= length:
        sticks.append(short/2)
    else:
        sticks.append(short/2)
        sticks.append(short/2)
print(len(sticks))