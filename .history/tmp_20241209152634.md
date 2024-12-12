#### 0. 单元格类（Cell）

```python
class Cell:
    def __init__(self, coordinate, adjacent_cells, bordering_cells, boundary_type, cell_type, occupier):
        self.coordinate = coordinate  # 坐标：横坐标(列号)为大写字母，纵坐标(行号)为数字
        self.adjacent_cells = adjacent_cells  # 相邻单元格：即其上、下和左上、左下、右上、右下6个单元格(边界单元格除外)
        self.bordering_cells = bordering_cells  # 毗邻单元格：即相邻单元格再往外扩展一圈后的单元格，加上相邻单元格一共18个
        self.boundary_type = boundary_type  # 边界类型：分为河流和普通边界
        self.cell_type = cell_type  # 单元格类型：分为城市、道路、树林、山脉、荒地
        self.occupier = occupier  # 占领者：分为红方占领、蓝方占领、无人占领

    # 边界类型取值范围字典
    boundary_type_dict = {
        0: "河流",
        1: "普通边界"
    }

    # 单元格类型取值范围字典
    cell_type_dict = {
        0: "城市",
        1: "道路",
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
```

在这个单元格类（Cell）的设计中，我们定义了以下属性：

- `coordinate`：坐标，由横坐标（列号，大写字母）和纵坐标（行号，数字）组成。
- `adjacent_cells`：相邻单元格，指的是直接相邻的6个单元格（不包括边界单元格）。
- `bordering_cells`：毗邻单元格，指的是包括相邻单元格在内的扩展一圈的单元格，总共18个。
- `boundary_type`：边界类型，使用字典`boundary_type_dict`来表示取值范围，0代表河流，1代表普通边界。
- `cell_type`：单元格类型，使用字典`cell_type_dict`来表示取值范围，0代表城市，1代表道路，2代表树林，3代表山脉，4代表荒地。
- `occupier`：占领者，使用字典`occupier_dict`来表示取值范围，0代表无人占领，1代表红方占领，2代表蓝方占领。

这样的设计可以确保单元格类的属性清晰且易于管理，同时也方便在代码中通过字典快速查找和理解各个属性的具体含义。
