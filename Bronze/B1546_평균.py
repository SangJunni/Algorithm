lecture_no = input()
scores = input().split()
scores = list(map(int, scores))
print(sum(scores)/max(scores)*100/int(lecture_no))