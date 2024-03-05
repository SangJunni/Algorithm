from bisect import bisect_left, bisect_right
n = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
m = int(input())
find_list = list(map(int, input().split()))
for d in find_list:
    num = bisect_right(num_list, d) - bisect_left(num_list, d)
    print(num, end=' ')
#내장 함수 count 사용 시 시간 초과
#정렬 후 bisect 라이브러리 사용