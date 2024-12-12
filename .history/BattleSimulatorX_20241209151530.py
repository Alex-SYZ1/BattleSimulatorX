from utils.constants import *
from typing import IO, List, Dict, Union,Int
class Board():
    def __init__(self, size):
        self.size = size
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        

class Cell:
    __slots__ = ('coordinate', 'adjacent_cells', 'bordering_cells', 'boundaries_type', 'cell_type')
    def __init__(self, 
                 coordinate:tuple[int,int], 
                 boundaries_type:dict[int:int] = Constants.Cell.boundaries_type, 
                 cell_type:int = Constants.Cell.cell_type, 
                 current_army:Union[Amry,None] = None,
                 occupier:int = Constants.Cell.occupier):
        """_summary_

        Args:
            coordinate (tuple[int,int]): 坐标：横坐标和纵坐标数字元组
            boundaries_type (dict[int:int], optional): 边界类型：分为河流和普通边界. Defaults to Constants.Cell.boundaries_type.
            cell_type (int, optional): 单元格类型：分为城市、道路、树林、山脉、荒地. Defaults to Constants.Cell.cell_type.
            current_army (Union[Amry,None], optional): 驻扎军队对象. Defaults to None.
            occupier (int, optional): 占领方：分为红方占领、蓝方占领、无人占领. Defaults to Constants.Cell.occupier.
        """
        self.coordinate = coordinate  
        self.boundaries_type = boundaries_type  
        self.cell_type = cell_type  
        self.occupier = occupier 
        self.current_army = current_army
    
        self.adjacent_cells = self.get_adjacent_cells(1)  
        self.bordering_cells = self.adjacent_cells + self.get_adjacent_cells(2) 
    def get_coordinate(self,return_typle = str):
        # 返回单元格的坐标
        coordinate_tuple = (CoordinateUtil.get_column_letter(self.coordinate[0]),self.coordinate[1])
        return f"{coordinate_tuple[0]}{coordinate_tuple[1]}" if return_typle == str else coordinate_tuple

    def get_adjacent_cells(self, circle_number):
        # 相邻单元格：即其上、下和左上、左下、右上、右下6个单元格(边界单元格除外)
        # 根据圈数返回相邻单元格列表
        if circle_number == 1:
            return self.adjacent_cells# 具体实现
        elif circle_number == 2:
            return self.bordering_cells
        else:
            raise ValueError("Circle number must be 1 or 2")

    def get_boundary_type(self, edge_number):
        # 根据边编号返回边界类型
        if 1 <= edge_number <= 6:
            return self.boundary_type[edge_number - 1]
        else:
            raise ValueError("Edge number must be between 1 and 6")

    def get_cell_type(self):
        # 返回单元格类型
        return self.cell_type

    def get_occupier(self):
        # 返回单元格的占领者
        return self.occupier

    def change_occupier(self, new_occupier):
        # 更新单元格的占领者
        self.occupier = new_occupier