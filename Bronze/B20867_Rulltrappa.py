m, s, g = map(int, input().split())
a,b = map(float, input().split())
l,r = map(int, input().split())

lwait = l / a
rwait = r / b

# 프리스크스가 점프하는 횟수 계산
ls = (m + g - 1) // g  # m을 g로 나누고 올림 처리
rs = (m + s - 1) // s  # m을 s로 나누고 올림 처리

# 결과 비교 및 출력
if ls < rs:
    if ls + lwait < rs + rwait:
        print("friskus")
    else:
        print("latmask")
else:
    if ls + lwait < rs + rwait:
        print("friskus")
    else:
        print("latmask")