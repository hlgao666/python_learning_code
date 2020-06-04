# 继承和多态
class Mannal:
    def walk(self):
        print('walk')


class Dog(Mannal):
    def bark(self):
        print('wow')


class Cat(Mannal):
    def miao(self):
        print('miao')


dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.miao()
