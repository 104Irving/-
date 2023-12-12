import pygame
import sys
import time
from random import randint

pygame.init()
WHITE = (255, 255, 255)  # 白色
BLACK = (0, 0, 0)  # 黑色


class Tabel(object):
    # 康威生命游戏的局面是一个类

    def __init__(self, line, roll, start):
        self.start = start
        size = (line*10, roll*10)
        self.screen = pygame.display.set_mode(size)

        # 设置窗口标题
        pygame.display.set_caption("康威生命游戏")

        self.line = line
        self.roll = roll
        self.list = [[0 for y in range(self.roll+2)] for x in range(self.line+2)]
        self.relist = [[0 for y in range(self.roll+2)] for x in range(self.line+2)]

    def table_print(self, a, b):
        # 玩家绘制初始图形
        self.list[a][b] = 1

    def random_generate(self):
        # 生成一个随机的开局
        for i in range(self.line):
            for j in range(self.roll):
                self.list[i][j] = randint(0, 1)

    def cell_states(self, a, b):  # 检查每一个单元格的状态，并根据环境运算出下个状态，并储存在relist列表中
        
        num = (self.list[a-1][b-1] + self.list[a-1][b] +
               self.list[a-1][b+1] + self.list[a][b-1] +
               self.list[a][b+1] + self.list[a+1][b-1] +
               self.list[a+1][b] + self.list[a+1][b+1])
        # 统计一个单元格周围八个单元格中活细胞的数目

        # 生命 = 死亡，且周围存活生命体数量= 3 ，则该生命获得新生。
        if self.list[a][b] == 0:
            if num == 3:
                self.relist[a][b] = 1
            else:  # 否则维持原状，但是要输入到relist里
                self.relist[a][b] = 0

        # If 生命 = 存活，且周围存活生命体数量>3 或 周围存活生命体数量<2 ，则该生命死亡。
        else:
            if num == 3 or num == 2:
                self.relist[a][b] = 1
            else:  # 否则维持原状，但是要输入到relist里
                self.relist[a][b] = 0
    
    def table_change(self):

        for i in range(self.line):  # 横坐标
            if i == 0:  # 检验边界，边界的单元格不用判断，始终视为0
                continue
            for j in range(self.roll):  # 纵坐标
                if j == 0:  # 检验边界，边界的单元格不用判断，始终视为0
                    continue
                self.cell_states(i, j)

        # for i in range(self.line):
        #     for j in range(self.roll):
        #         print(str(self.list[i][j]), end=" ")
        #     print()
        #
        # print()
        #
        # for i in range(self.line):
        #     for j in range(self.roll):
        #         print(str(self.relist[i][j]), end=" ")
        #     print()

        # 游戏内容更新
        for i in range(self.line):
            for j in range(self.roll):
                self.list[i][j] = self.relist[i][j]
                self.relist[i][j] = 0

    def table_show(self):
        cell_rect = [0, 0, self.line*10, self.roll*10]
        pygame.draw.rect(self.screen, BLACK, cell_rect)

        # 画白色边界线 横线
        for i in range(self.line):
            start_pos = (i*10, 0)
            end_pos = (i*10, self.roll*10)
            pygame.draw.line(self.screen, WHITE, start_pos, end_pos, 1)

        # 画白色边界线 竖线
        for i in range(self.roll):
            start_pos = (0, i*10)
            end_pos = (self.line*10, i*10)
            pygame.draw.line(self.screen, WHITE, start_pos, end_pos, 1)

        for i in range(self.line):
            for j in range(self.roll):
                # 绘制白色方格
                if self.list[i][j] == 1:
                    cell_rect = [i*10, j*10, 10, 10]
                    pygame.draw.rect(self.screen, WHITE, cell_rect)


# 以下是测试用代码


def __main__():
    game1 = Tabel(100, 50, 200)
    a = True
    game1.random_generate()

    while a:
        # 监听事件
        for event in pygame.event.get():

            # 退出程序的监听
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # 鼠标事件的监听
            if event.type == pygame.MOUSEBUTTONDOWN:  # 鼠标按下
                a, b = pygame.mouse.get_pos()
                game1.table_print(a//10, b//10)

            # 键盘事件的监听
            if event.type == pygame.KEYDOWN:
                a = False

        game1.table_show()
        pygame.display.update()

    while True:
        for event in pygame.event.get():

            # 退出程序的监听
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        game1.table_change()
        game1.table_show()
        pygame.display.update()
        time.sleep(0.5)


__main__()


# game1 = Tabel(7, 7)
# r = True
# game1.table_print(2, 3)
# game1.table_print(3, 3)
# game1.table_print(4, 3)
# while r:
#     a, b = input("input").split()
#     if a == "-1":
#         r = False
#
#     game1.table_print(int(a), int(b))
#
#     for i in range(game1.line):
#         for j in range(game1.roll):
#             print(str(game1.list[i][j]), end=" ")
#         print()

# while True:
#     s = input("input")
#     game1.table_change()
