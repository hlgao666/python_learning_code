# 变量赋值
myName = 'tom'
print(myName)

# list -- 列表
a = [10,20,30]
print(type(a))

# tuple -- 元组
b = (10,20,30)
print(type(b))

# set -- 集合
c = {10,20,30}
print(type(c))

# dict -- 字典 -- 键值对
d = {'name':'tom' , 'age':18}
print(type(d))

age = 18
print("我的年龄是：%d岁" % age)

# 浮点数格式化输出，需在f前加.数字，输出65.000
weight = 65.5
print("我的体重是%.3f斤" % weight)

# 格式化输出,输出001，共3位，不足用0补齐
id = 1
print("我的id是%03d" % id)

# 格式化输出多个变量
print('我的名字是%s,今年%s岁了，体重是%s斤' % (myName, age, weight))

# f表达式 语法 -- f'{表达式}'
print(f'我的名字是{myName},今年{age}岁了，体重是{weight}斤')

# print结束符 -- 默认（end='\n'）,可自定义修改,输出为 "age...hello"
print(age, end='...')
print("hello")

# input('提示信息')   input接受到的数据类型都是字符串
password = input('请输入密码：')
print(f'您的密码为：{password}')
print(type(password))

# 转换数据类型,password -- int
password = int(password)
print(type(password))

'''
tuple() -- 转换为元组类型
list() -- 转换为列表类型
'''

a = (10, 20, 30)    # 元组类型
print(a)
print(type(list(a)))

# eval() -- 计算字符串中的有效的python表达式，并返回一个对象
b = '[1, 2, 3]'         # b是字符串
print(eval(b))          # 返回[1, 2, 3], 是个列表对象
