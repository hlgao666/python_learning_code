numbers = [10, 20, 30, 20, 10, 40]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
else:
    print(unique)
