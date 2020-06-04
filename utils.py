
def find_max(numbers):
    max_num = 0
    for num in numbers:
        if max_num < num:
            max_num = num
    return max_num

