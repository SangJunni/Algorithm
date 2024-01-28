#높이는 무조건 2이므로 가로 직사각형을 넣을 경우 2개가 필요
#이를 활용하면 너비가 2인 직사각형을 놓을 수 있는 최대 경우의 수를 구해서 리스트로 만들어가면서 경우의 수 게산
from itertools import permutations
n = int(input())
max_w = n//2
min_w = n%2
choice = [1]*min_w + [2] * max_w
case = 0
while True:
    temp = list(set(permutations(choice)))
    print(choice)
    print(temp)
    if 2 in choice:
        choice.remove(2)
        choice.append(1)
        choice.append(1)
    else:
        case += len(temp)
        break
    case += len(temp)
print(case)
#이 방식으로는 시간초과