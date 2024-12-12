
class Board():
    def __init__(self, size):
        self.size = size
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        

class Cell:
    def __init__(self, coordinate, boundary_type = 0, cell_type = 0, occupier = 0):
        self.coordinate = coordinate  # 坐标：横坐标(列号)为大写字母，纵坐标(行号)为数字
        self.adjacent_cells = adjacent_cells  # 相邻单元格：即其上、下和左上、左下、右上、右下6个单元格(边界单元格除外)
        self.bordering_cells = bordering_cells  # 毗邻单元格：即相邻单元格再往外扩展一圈后的单元格，加上相邻单元格一共18个
        self.boundary_type = boundary_type  # 边界类型：分为河流和普通边界
        self.cell_type = cell_type  # 单元格类型：分为城市、道路、树林、山脉、荒地
        self.occupier = occupier  # 占领者：分为红方占领、蓝方占领、无人占领
    
    def get_coordinate(self):
        # 返回单元格的坐标
        return self.coordinate

    def get_adjacent_cells(self, circle_number):
        # 根据圈数返回相邻单元格列表
        if circle_number == 1:
            return self.adjacent_cells
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