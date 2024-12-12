
# 棋盘类(Board)
BoardRowNum,BoardColNum = 7,14

# 单元格类(Cell)
class CellDefault
# 边界类型取值范围字典
boundary_type_dict = {
    0: "普通边界",
    1: "河流"
}

# 单元格类型取值范围字典
cell_type_dict = {
    0: "道路",
    1: "城市",
    2: "树林",
    3: "山脉",
    4: "荒地"
}

# 占领者取值范围字典
occupier_dict = {
    0: "无人占领",
    1: "红方占领",
    2: "蓝方占领"
}


class Constants:
    class Board:
        ROW_NUM = 7
        COL_NUM = 14
        
        class code2name:
            boundary_type_dict = {
            0: "普通边界",
            1: "河流"
        }

            # 单元格类型取值范围字典
            cell_type_dict = {
                0: "道路",
                1: "城市",
                2: "树林",
                3: "山脉",
                4: "荒地"
            }

            # 占领者取值范围字典
            occupier_dict = {
                0: "无人占领",
                1: "红方占领",
                2: "蓝方占领"
            }

    class Cell:
        class code2name:
            
        DEFAULT = None  # 如果有默认值可以在这里设置

        class BoundaryType:
            COMMON = 0
            RIVER = 1

        class CellType:
            ROAD = 0
            CITY = 1
            FOREST = 2
            MOUNTAIN = 3
            WASTELAND = 4

        boundary_type_dict = {
            BoundaryType.COMMON: "普通边界",
            BoundaryType.RIVER: "河流"
        }

        cell_type_dict = {
            CellType.ROAD: "道路",
            CellType.CITY: "城市",
            CellType.FOREST: "树林",
            CellType.MOUNTAIN: "山脉",
            CellType.WASTELAND: "荒地"
        }


