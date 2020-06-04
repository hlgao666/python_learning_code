class Pointer:

    # 定义构造器，初始化
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')


pointer1 = Pointer(2, 3)
pointer1.draw()         # 调用对象方法
print(pointer1.x)

pointer1.x = 10         # 重新定义私有变量
print(pointer1.x)

pointer2 = Pointer(y=10, x=20)
print(pointer2.x)
