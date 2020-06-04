import random


class Dice:

    def roll(self):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        return x, y             # 不加括号时，默认返回tuple类型


dice = Dice()
print(dice.roll())
