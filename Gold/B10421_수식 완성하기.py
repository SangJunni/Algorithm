def is_valid(tmp, idx, digits, numbers):
    if len(tmp) != digits[idx]:
        return False
    for char in tmp:
        if int(char) not in numbers:
            return False
    return True

def able(a, b, N, digits, numbers):
    if not is_valid(str(a * b), N - 1, digits, numbers):
        return False
    b_str = str(b)
    for i in range(digits[1]):
        if not is_valid(str(a * int(b_str[i])), N - 2 - i, digits, numbers):
            return False
    return True

def selectB(blen, bval, aval, digits, numbers, K, answer, N):
    if blen == digits[1]:
        if able(aval, bval, N, digits, numbers):
            answer[0] += 1
        return
    for i in range(K):
        selectB(blen + 1, bval + (numbers[i]) * (10 ** blen), aval, digits, numbers, K, answer, N)

def selectA(alen, aval, digits, numbers, K, answer, N):
    if alen == digits[0]:
        selectB(0, 0, aval, digits, numbers, K, answer, N)
        return
    for i in range(K):
        selectA(alen + 1, aval + (numbers[i]) * (10 ** alen), digits, numbers, K, answer, N)



N = int(input())
digits = list(map(int, input().split()))
K = int(input())
numbers = list(map(int, input().split()))

answer = [0]
selectA(0, 0, digits, numbers, K, answer, N)
print(answer[0])