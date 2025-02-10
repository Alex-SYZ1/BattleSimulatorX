# Board.py
from utils.constants import *

class Board:
    """由棋子、格子构成的棋盘，是对象的嵌套体
    - 方法：
    - initializeBoard(): 初始化棋盘，包括地图、地形、兵种等。
    - getCell(x, y): 获取指定坐标的格子信息。
    - setCell(x, y, cell): 设置指定坐标的格子信息。
    - getVision(x, y): 获取指定坐标的视野范围。
    - getCombatPower(x, y): 获取指定坐标的战斗力。
    - getMovePower(x, y): 获取指定坐标的移动力。
    """
    def __init__(self):
        1