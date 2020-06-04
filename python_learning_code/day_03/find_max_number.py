numbers = [13, 39, 57, 23, 45, 58]
max_num = 0
for num in numbers:
    if max_num < num:
        max_num = num
else:
    print(f'The Max Number is {max_num}')

numbers = [10, 20, 30, 40, 10, 50]
numbers.sort()
print(numbers.count(10))
print(numbers)
print('...')
numbers.reverse()
print(numbers)
