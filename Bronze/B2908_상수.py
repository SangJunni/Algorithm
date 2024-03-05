str1, str2 = map(str, input().split())
print(max(int(str1[::-1]), int(str2[::-1])))
