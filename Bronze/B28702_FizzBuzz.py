for i in range(3):
    temp = input()
    if temp.isdigit():
        num = int(temp) + 3 - i
if num % 3 != 0 and num % 5 != 0:
    print(num)
else:
    print('Fizz'*(num%3 == 0) + 'Buzz'*(num%5 ==0))