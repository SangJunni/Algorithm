# 입력
N = int(input())
promises = []

# 공약 입력 및 저장
for _ in range(N):
    promise = input().strip()
    promises.append(promise)

# Rick Astley의 공약
rick_astley_promise = [
    "Never gonna give you up",
    "Never gonna let you down",
    "Never gonna run around and desert you",
    "Never gonna make you cry",
    "Never gonna say goodbye",
    "Never gonna tell a lie and hurt you",
    "Never gonna stop"
]

# 공약 검사
def check_promises(promises, rick_astley_promise):
    for promise in promises:
        if promise not in rick_astley_promise:
            return "Yes"
    return "No"

result = check_promises(promises, rick_astley_promise)

# 출력
print(result)