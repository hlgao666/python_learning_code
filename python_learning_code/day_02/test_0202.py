# 猜拳游戏
import random

game_set = {0: '石头', 1: '剪刀', 2: '布'}

# 玩家出
player = int(input('请输入数字：（0-石头，1-剪刀，2-布）'))

# 电脑出
computer = random.randint(0, 2)

# 判断输赢

# 玩家赢
if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
    print(f'您出：{game_set[player]},\n电脑出:{game_set[computer]},\n您获胜')
    # 平局
elif player == computer:
    print(f'您出：{game_set[player]},\n电脑出：{game_set[computer]},\n您和电脑平局')
else:
    print(f'您出：{game_set[player]},\n电脑出：{game_set[computer]},\n您输了')

print("游戏结束")
