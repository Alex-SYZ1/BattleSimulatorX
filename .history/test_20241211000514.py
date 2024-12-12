import unittest
from unittest.mock import patch
from BattleSimulatorX import Cell, Constants

class TestGetAdjacentCells(unittest.TestCase):
    
    '''
    测试第一圈相邻单元格获取，位于棋盘中间位置
    circle_number=1, start_index=1, self.coordinate=(5,5), mock Constants.BoardCst.ODD_δx6 和 Constants.BoardCst.EVEN_δx6 返回相应的坐标偏移列表
    '''
    @patch('BattleSimulatorX.Constants.BoardCst.ODD_δx6', [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1)])
    @patch('BattleSimulatorX.Constants.BoardCst.EVEN_δx6', [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1)])
    def test_get_adjacent_cells_middle_odd(self):
        cell = Cell((5, 5))
        expected_result = {
            1: (4, 4), 2: (4, 5), 3: (4, 6), 4: (5, 4), 5: (5, 6), 6: (6, 4)
        }
        self.assertEqual(cell.get_adjacent_cells(1), expected_result)

    '''
    测试第二圈相邻单元格获取，位于棋盘边缘位置
    circle_number=2, start_index=1, self.coordinate=(1,1), mock Constants.BoardCst.ODD_δx12 和 Constants.BoardCst.EVEN_δx12 返回相应的坐标偏移列表
    '''
    @patch('BattleSimulatorX.Constants.BoardCst.ODD_δx12', [(-2, -2), (-2, -1), (-2, 0), (-2, 1), (-2, 2), (-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2), (0, -2), (0, -1), (0, 1), (0, 2), (1, -2), (1, -1), (1, 0), (1, 1), (1, 2), (2, -2), (2, -1), (2, 0), (2, 1), (2, 2)])
    @patch('BattleSimulatorX.Constants.BoardCst.EVEN_δx12', [(-2, -2), (-2, -1), (-2, 0), (-2, 1), (-2, 2), (-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2), (0, -2), (0, -1), (0, 1), (0, 2), (1, -2), (1, -1), (1, 0), (1, 1), (1, 2), (2, -2), (2, -1), (2, 0), (2, 1), (2, 2)])
    def test_get_adjacent_cells_edge_even(self):
        cell = Cell((1, 1))
        expected_result = {
            1: (-1, -1), 2: (-1, 0), 3: (-1, 1), 4: (0, -1), 5: (0, 1), 6: (1, -1),
            7: (1, 0), 8: (1, 1), 9: (2, -1), 10: (2, 0), 11: (2, 1), 12: (3, -1),
            13: (3, 0), 14: (3, 1), 15: (4, -1), 16: (4, 0), 17: (4, 1), 18: (5, -1),
            19: (5, 0), 20: (5, 1)
        }
        self.assertEqual(cell.get_adjacent_cells(2), expected_result)

    '''
    测试第一圈相邻单元格获取，位于棋盘角落位置
    circle_number=1, start_index=1, self.coordinate=(1,1), mock Constants.BoardCst.ODD_δx6 和 Constants.BoardCst.EVEN_δx6 返回相应的坐标偏移列表
    '''
    @patch('BattleSimulatorX.Constants.BoardCst.ODD_δx6', [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1)])
    @patch('BattleSimulatorX.Constants.BoardCst.EVEN_δx6', [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1)])
    def test_get_adjacent_cells_corner_odd(self):
        cell = Cell((1, 1))
        expected_result = {
            1: None, 2: None, 3: None, 4: None, 5: None, 6: None
        }
        self.assertEqual(cell.get_adjacent_cells(1), expected_result)

    '''
    测试非法圈数输入，应抛出异常
    circle_number=3, start_index=1, self.coordinate=(5,5)
    '''
    def test_get_adjacent_cells_invalid_circle(self):
        cell = Cell((5, 5))
        with self.assertRaises(ValueError):
            cell.get_adjacent_cells(3)

    '''
    测试边界条件，当start_index大于实际可返回的单元格数量时
    circle_number=1, start_index=10, self.coordinate=(1,1), mock Constants.BoardCst.ODD_δx6 和 Constants.BoardCst.EVEN_δx6 返回较小的坐标偏移列表
    '''
    @patch('BattleSimulatorX.Constants.BoardCst.ODD_δx6', [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1)])
    @patch('BattleSimulatorX.Constants.BoardCst.EVEN_δx6', [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1)])
    def test_get_adjacent_cells_start_index_too_large(self):
        cell = Cell((1, 1))
        expected_result = {}
        self.assertEqual(cell.get_adjacent_cells(1, start_index=10), expected_result)

    '''
    测试棋盘边缘单元格，确保不会返回超出棋盘范围的单元格
    circle_number=2, start_index=1, self.coordinate=(1,1), mock Constants.BoardCst.ODD_δx12 和 Constants.BoardCst.EVEN_δx12 返回部分超出棋盘范围的坐标偏移列表
    '''
    @patch('BattleSimulatorX.Constants.BoardCst.ODD_δx12', [(-2, -2), (-2, -1), (-2, 0), (-2, 1), (-2, 2), (-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2), (0, -2), (0, -1), (0, 1), (0, 2), (1, -2), (1, -1), (1, 0), (1, 1), (1, 2), (2, -2), (2, -1), (2, 0), (2, 1), (2, 2)])
    @patch('BattleSimulatorX.Constants.BoardCst.EVEN_δx12', [(-2, -2), (-2, -1), (-2, 0), (-2, 1), (-2, 2), (-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2), (0, -2), (0, -1), (0, 1), (0, 2), (1, -2), (1, -1), (1, 0), (1, 1), (1, 2), (2, -2), (2, -1), (2, 0), (2, 1), (2, 2)])
    def test_get_adjacent_cells_edge_within_bounds(self):
        cell = Cell((1, 1))
        expected_result = {
            1: None, 2: None, 3: None, 4: None, 5: None, 6: None,
            7: None, 8: None, 9: None, 10: None, 11: None, 12: None,
            13: None, 14: None, 15: None, 16: None, 17: None, 18: None
        }
        self.assertEqual(cell.get_adjacent_cells(2), expected_result)