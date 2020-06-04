class Person:

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Talk with {self.name}')


man1 = Person('Jack')
man1.talk()
