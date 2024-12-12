import unittest
from unittest.mock import patch, MagicMock
#此处是其他需要import的信息，注意必须导入被测函数的相关依赖
from BattleSimulatorX import Board, Cell, Army

class TestChangeCurrentArmy(unittest.TestCase):
    def setUp(self):
        self.cell = Cell((1, 1))

    '''
    测试单元格更新军队时，传入有效的新军队对象
    new_army=Army(name="Red Army")
    /
    '''
    def test_change_current_army_with_valid_army(self):
        new_army = Army(name="Red Army")
        self.cell.change_current_army(new_army)
        self.assertEqual(self.cell.occupier, new_army)

    '''
    测试单元格更新军队时，传入None作为新军队对象，模拟清除驻扎军队的情况
    new_army=None
    /
    '''
    def test_change_current_army_with_none(self):
        self.cell.change_current_army(None)
        self.assertIsNone(self.cell.occupier)

    '''
    测试单元格更新军队时，传入非预期类型的新军队对象，例如整数，检查是否有类型检查机制
    new_army=123
    /
    '''
    def test_change_current_army_with_invalid_type(self):
        with self.assertRaises(TypeError):
            self.cell.change_current_army(123)

    '''
    测试单元格更新军队时，传入具有特殊字符的军队名称，确保系统能正确处理特殊字符
    new_army=Army(name="Green &amp; Blue Army")
    /
    '''
    def test_change_current_army_with_special_characters(self):
        new_army = Army(name="Green & Blue Army")
        self.cell.change_current_army(new_army)
        self.assertEqual(self.cell.occupier, new_army)

    '''
    测试单元格更新军队时，传入一个空字符串作为军队名称，检查系统是否能处理空字符串情况
    new_army=Army(name="")
    /
    '''
    def test_change_current_army_with_empty_string(self):
        new_army = Army(name="")
        self.cell.change_current_army(new_army)
        self.assertEqual(self.cell.occupier, new_army)

    '''
    测试单元格更新军队时，传入一个极长字符串作为军队名称，检查系统是否能处理超长字符串
    new_army=Army(name="A" * 1000)
    /
    '''
    def test_change_current_army_with_long_string(self):
        long_name = "A" * 1000
        new_army = Army(name=long_name)
        self.cell.change_current_army(new_army)
        self.assertEqual(self.cell.occupier, new_army)

if __name__ == '__main__':
    unittest.main()