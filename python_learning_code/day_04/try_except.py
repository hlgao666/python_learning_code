# try-except 处理异常
try:
    age = int(input('Age: '))
    print(age)
except ValueError:
    print('Invalid value')
