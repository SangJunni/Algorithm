import sys
import bisect
answer = sys.maxsize


def search(v1, v2, v3):
    global answer
    # v1, v2를 이용해 최대 최소값의 모든 경우의 수를 찾는다.
    for num1 in v1:
        for num2 in v2:
            # v1, v2를 기준으로 최대 최소값을 만들었다면
            max_num = max(num1, num2)
            min_num = min(num1, num2)

            # 이분 탐색을 통해 v3에서 사잇값이 존재하는지 찾는다.
            max_idx = bisect.bisect_right(v3, max_num) - 1
            min_idx = bisect.bisect_right(v3, min_num)

            # 사잇값이 존재한다면 답을 갱신한다.
            if 0 <= max_idx < len(v3) and 0 <= min_idx <= max_idx:
                answer = min(answer, abs(max_num - min_num))


a, b, c = map(int, input().split())
player1 = sorted(list(map(int, input().split())))
player2 = sorted(list(map(int, input().split())))
player3 = sorted(list(map(int, input().split())))

# 모든 경우의 수를 찾는다.
search(player1, player2, player3)
search(player1, player3, player2)
search(player2, player3, player1)

print(answer)
