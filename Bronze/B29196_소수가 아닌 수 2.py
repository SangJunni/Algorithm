def find_fraction(k):
    # 소수 k를 10^9까지 확장하여 정수로 만든다.
    extended_k = int(k * 1e9)

    # 분수 p/q를 구성한다.
    p = extended_k
    q = int(1e9)

    # 절대오차와 상대오차 조건을 확인한다.
    abs_error = abs(p / q - k)
    rel_error = abs_error / k if k != 0 else abs_error

    if abs_error <= 1e-6 or rel_error <= 1e-6:
        return "YES\n{} {}\n".format(p, q)
    else:
        return "NO\n"


# 입력 받기
k = float(input())

# 분수 찾기
result = find_fraction(k)
print(result)