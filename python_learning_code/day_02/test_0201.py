# 多重判断
age = int(input("请输入您的年龄："))
if age < 18:
    print(f'您的年龄为{age}岁，需要读书')
elif 18 <= age <= 60:
    print(f'您的年龄为{age}岁，需要工作')
else:
    print(f'您可以退休了')
print('系统关闭')
