def solution(food_times, k):
    start = 0
    before_k = k
    for i in range(1, max(food_times)):
        food_num = [x for x in food_times if x >= i]
        if before_k > len(food_num):
            before_k -= len(food_num)
        else:
            left_food = [x for x, value in enumerate(food_times) if value >= i]
            if before_k == len(left_food):
                start = left_food[0]
            else:
                start = left_food[before_k]

    answer = start + 1
    return answer

food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))
