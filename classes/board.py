# Board.py
import utils.constants as Constants
from cell import Cell

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
        # 引入常量，遍历生成单元格
        self.BoardCst = Constants.BoardCst()
        self.max_row = self.BoardCst.ROW_NUM
        self.max_col = self.BoardCst.COL_NUM
        self.initial_settings = Constants.DictAttr(red_vision = self.BoardCst.RED_INIT_VISION,
                                         blue_vision = self.BoardCst.BLUE_INIT_VISION,
                                         river_board = self.BoardCst.RIVER_BOARD)
    def initializeBoard(self):
        grid = Constants.DictAttr()
    def setCell(self, x, y, ):
        """设置指定坐标的格子信息"""
        initial_boundaries_type = Constants.CellCst.boundaries_type()
        current_Cell = Cell(coordinate=(x,y),)