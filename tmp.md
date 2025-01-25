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
- `boundary_type`：边界类型，使用字典 `boundary_type_dict`来表示取值范围，0代表河流，1代表普通边界。
- `cell_type`：单元格类型，使用字典 `cell_type_dict`来表示取值范围，0代表城市，1代表道路，2代表树林，3代表山脉，4代表荒地。
- `occupier`：占领者，使用字典 `occupier_dict`来表示取值范围，0代表无人占领，1代表红方占领，2代表蓝方占领。

这样的设计可以确保单元格类的属性清晰且易于管理，同时也方便在代码中通过字典快速查找和理解各个属性的具体含义。


当然，以下是Unit类的属性和方法的中英文介绍：

### 属性（Attributes）：

- **Type (str)**：

  - 英文：The type of the unit.
  - 中文：部队的类型。
- **Quantity (int)**：

  - 英文：The number of units of this type.
  - 中文：该类型的部队数量。
- **CombatPower (int)**：

  - 英文：The combat strength of the unit.
  - 中文：部队的战斗力。
- **MovementPoints (int)**：

  - 英文：The maximum number of格子 a unit can move in one turn.
  - 中文：部队在一回合中能移动的最大格子数。
- **Cost (int)**：

  - 英文：The cost to produce or deploy the unit.
  - 中文：生产或部署该部队的成本。
- **TerrainRestrictions (dict)**：

  - 英文：A dictionary defining movement penalties for different terrains.
  - 中文：定义不同地形上移动力消耗的字典。
- **Vision (int)**：

  - 英文：The range within which the unit can attack and detect enemy units.
  - 中文：部队能够攻击和探测敌方部队的视野范围。
- **CurrentPosition (tuple)**：

  - 英文：The current (x, y) coordinates of the unit on the game map.
  - 中文：部队在游戏地图上的当前坐标（x, y）。
- **Status (str)**：

  - 英文：The current status of the unit, e.g., 'normal', 'damaged', 'retreated'.
  - 中文：部队的当前状态，例如“正常”、“受损”、“撤退”。

### 方法（Methods）：

- **__init__(type, quantity, x, y)**：

  - 英文：Initializes a new unit with type, quantity, and coordinates.
  - 中文：使用类型、数量和坐标初始化一个新的部队。
- **move(x, y)**：

  - 英文：Moves the unit to the specified coordinates.
  - 中文：将部队移动到指定的坐标。
- **attack(target)**：

  - 英文：Attacks a target unit.
  - 中文：攻击目标部队。
- **retreat()**：

  - 英文：Retreats the unit to a specified position.
  - 中文：使部队撤退到指定位置。
- **getCombatPower()**：

  - 英文：Retrieves the unit's combat power.
  - 中文：获取部队的战斗力。
- **getMovementPoints()**：

  - 英文：Retrieves the unit's movement points.
  - 中文：获取部队的移动力。
- **adjustQuantity(change)**：

  - 英文：Adjusts the quantity of the unit.
  - 中文：调整部队的数量。
- **getVision()**：

  - 英文：Retrieves the unit's vision range.
  - 中文：获取部队的视野范围。
- **updateTerrainAdaptability(terrain, cost)**：

  - 英文：Updates the movement cost for a specific terrain type.
  - 中文：更新特定地形类型的移动力消耗。
- **setPosition(x, y)**：

  - 英文：Sets the current position of the unit.
  - 中文：设置部队的当前位置。
- **updateStatus(status)**：

  - 英文：Updates the status of the unit.
  - 中文：更新部队的状态。
- **getStatus()**：

  - 英文：Retrieves the current status of the unit.
  - 中文：检索部队的当前状态。
- **getTerrainAdaptability(terrain)**：

  - 英文：Retrieves the movement cost for a specific terrain type.
  - 中文：检索特定地形类型的移动力消耗。
- **getPosition()**：

  - 英文：Retrieves the current position of the unit.
  - 中文：检索部队的当前位置。



当然，以下是Unit类的属性和方法的中英文介绍：

### 属性（Attributes）：

- **Type (str)**：

  - 英文：The type of the unit.
  - 中文：部队的类型。
- **Quantity (int)**：

  - 英文：The number of units of this type.
  - 中文：该类型的部队数量。
- **CombatPower (int)**：

  - 英文：The combat strength of the unit.
  - 中文：部队的战斗力。
- **MovementPoints (int)**：

  - 英文：The maximum number of格子 a unit can move in one turn.
  - 中文：部队在一回合中能移动的最大格子数。
- **Cost (int)**：

  - 英文：The cost to produce or deploy the unit.
  - 中文：生产或部署该部队的成本。
- **TerrainRestrictions (dict)**：

  - 英文：A dictionary defining movement penalties for different terrains.
  - 中文：定义不同地形上移动力消耗的字典。
- **Vision (int)**：

  - 英文：The range within which the unit can attack and detect enemy units.
  - 中文：部队能够攻击和探测敌方部队的视野范围。
- **CurrentPosition (tuple)**：

  - 英文：The current (x, y) coordinates of the unit on the game map.
  - 中文：部队在游戏地图上的当前坐标（x, y）。
- **Status (str)**：

  - 英文：The current status of the unit, e.g., 'normal', 'damaged', 'retreated'.
  - 中文：部队的当前状态，例如“正常”、“受损”、“撤退”。

### 方法（Methods）：

- **__init__(type, quantity, x, y)**：

  - 英文：Initializes a new unit with type, quantity, and coordinates.
  - 中文：使用类型、数量和坐标初始化一个新的部队。
- **move(x, y)**：

  - 英文：Moves the unit to the specified coordinates.
  - 中文：将部队移动到指定的坐标。
- **attack(target)**：

  - 英文：Attacks a target unit.
  - 中文：攻击目标部队。
- **retreat()**：

  - 英文：Retreats the unit to a specified position.
  - 中文：使部队撤退到指定位置。
- **getCombatPower()**：

  - 英文：Retrieves the unit's combat power.
  - 中文：获取部队的战斗力。
- **getMovementPoints()**：

  - 英文：Retrieves the unit's movement points.
  - 中文：获取部队的移动力。
- **adjustQuantity(change)**：

  - 英文：Adjusts the quantity of the unit.
  - 中文：调整部队的数量。
- **getVision()**：

  - 英文：Retrieves the unit's vision range.
  - 中文：获取部队的视野范围。
- **updateTerrainAdaptability(terrain, cost)**：

  - 英文：Updates the movement cost for a specific terrain type.
  - 中文：更新特定地形类型的移动力消耗。
- **setPosition(x, y)**：

  - 英文：Sets the current position of the unit.
  - 中文：设置部队的当前位置。
- **updateStatus(status)**：

  - 英文：Updates the status of the unit.
  - 中文：更新部队的状态。
- **getStatus()**：

  - 英文：Retrieves the current status of the unit.
  - 中文：检索部队的当前状态。
- **getTerrainAdaptability(terrain)**：

  - 英文：Retrieves the movement cost for a specific terrain type.
  - 中文：检索特定地形类型的移动力消耗。
- **getPosition()**：

  - 英文：Retrieves the current position of the unit.
  - 中文：检索部队的当前位置。
