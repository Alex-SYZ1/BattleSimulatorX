from utils.constants import *
from typing import IO, List, Dict, Union
class Board():
    def __init__(self, size):
        self.size = size
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        

class Cell:
    """主要记录该单元格自身属性与相关对象情况及其变迁，不涉及作战"""
    # __slots__ = ('coordinate', 'adjacent_cells', 'bordering_cells', 'boundaries_type', 'cell_type')
    def __init__(self, 
                 coordinate:tuple[int,int], 
                 boundaries_type:dict[int:int] = Constants.CellCst.boundaries_type, 
                 cell_type:int = Constants.CellCst.cell_type, 
                 current_army:Union[None] = None,# Union[Amry]
                 occupier:int = Constants.CellCst.occupier):
        """根据参数设置该单元格的基本属性，并调用函数设置可变属性

        Args:
            coordinate (tuple[int,int]): 坐标：横坐标和纵坐标数字元组
            boundaries_type (dict[int:int], optional): 边界类型：分为河流和普通边界. Defaults to Constants.CellCst.boundaries_type.
            cell_type (int, optional): 单元格类型：分为城市、道路、树林、山脉、荒地. Defaults to Constants.CellCst.cell_type.
            current_army (Union[Amry,None], optional): 驻扎军队对象，考虑设置为编号，在战斗时再依据编号索引到对象. Defaults to None.
            occupier (int, optional): 占领方：分为红方占领、蓝方占领、无人占领. Defaults to Constants.CellCst.occupier.
        """
        self.coordinate = coordinate  
        self.boundaries_type = boundaries_type  
        self.cell_type = cell_type  
        self.occupier = occupier 
        self.current_army = current_army

        self.adjacent_cells = self.get_adjacent_cells(1)  
        self.bordering_cells = {**self.adjacent_cells, **self.get_adjacent_cells(2) }
        
    def get_coordinate(self,return_typle:Union[str,tuple] = str):
        """返回单元格的坐标，默认返回字符串格式"""
        coordinate_tuple = (CoordinateUtil.get_column_letter(self.coordinate[0]),self.coordinate[1])
        return f"{coordinate_tuple[0]}{coordinate_tuple[1]}" if return_typle == str else coordinate_tuple

    def get_adjacent_cells(self, circle_number):
        """根据圈数返回相邻单元格列表
        第一圈(相邻单元格)：即其上、下和左上、左下、右上、右下6个单元格(边界单元格除外)
        第二圈(毗邻单元格)：指的是包括相邻单元格在内的扩展一圈的单元格，总共18个。"""
        
        get_adj_by_change = lambda c,δx6:[(c[0]+δ_x,c[1]+δ_y) for δ_x,δ_y in δx6]
        check_adj_by_border = lambda c:(c[0] in range(1,Constants.BoardCst.COL_NUM+1)) and (c[1] in range(1,Constants.BoardCst.ROW_NUM+1))
        
        c_x,c_y = self.coordinate

        if circle_number == 1:
            if c_x%2 == 1:
                adjacent_cell_dict = {adj_index:(ajd_c if check_adj_by_border(ajd_c) else None) for adj_index,ajd_c in enumerate(get_adj_by_change(self.coordinate,Constants.BoardCst.ODD_δx6),1)}
            else:
                    adjacent_cell_dict = {adj_index:(ajd_c if check_adj_by_border(ajd_c) else None) for adj_index,ajd_c in enumerate(get_adj_by_change(self.coordinate,Constants.BoardCst.EVEN_δx6),1)}
                    
            return adjacent_cell_dict
        
        elif circle_number == 2:
            adjacent2_cell_dict = {adj_index:(ajd_c if check_adj_by_border(ajd_c) else None) for adj_index,ajd_c in enumerate(get_adj_by_change(self.coordinate,(Constants.BoardCst.ODD_δx12 if c_x%2 ==1 else Constants.BoardCst.EVEN_δx12)),7)}
            
            return adjacent2_cell_dict
            
        else:
            raise ValueError("Circle number must be 1 or 2")
            

    def get_boundary_type(self, edge_number):
        # 根据边编号返回边界类型
        if 1 <= edge_number <= 6:
            return self.boundaries_type[edge_number - 1]
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
        
    def get_cuurent_army(self):
        # 返回单元格的驻扎军队
        return self.occupier

    def change_cuurent_army(self, new_army):
        # 更新单元格的驻扎军队
        self.occupier = new_army
        
if __name__ == "__main__":
    # for i in "ABCDEFGHIJKLMN":
    #     print(f"col_{i} = 0 0 0 0 0 0 0")
    test_cell = Cell((1,1))
    print("cell_type",test_cell.cell_type)
    print(test_cell.bordering_cells)