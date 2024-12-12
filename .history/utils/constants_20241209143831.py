class Constants:
    class Board:

        ROW_NUM = 7
        COL_NUM = 14
        
    class Cell:
        
        boundaries_type = {b_index:b_type for b_index,b_type in enumerate([0]*6,1)}
        cell_type = 0
        occupier = 0
        
        class code2name:
            # 单元格边界取值范围字典
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

