def solution(numbers):
    numbers = [str(x) for x in numbers]
    numbers.sort(key=lambda num : num*3, reverse = True)
    return str(int(''.join(numbers)))

numbers= [6, 10, 2]
result =solution(numbers)
print(result)