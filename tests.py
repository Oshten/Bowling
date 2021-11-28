# -*- coding: utf-8 -*-

import unittest

from errors import SumError
from bowling import PointsCounter

class BowlingTest(unittest.TestCase):

    def setUp(self) -> None:
        self.point_counter = PointsCounter('X4/34')

    def test_reigt_resalt(self):
        self.point_counter.game_resalt = 'X4/34-85--/'
        self.point_counter.start_counter()
        self.assertEqual(self.point_counter.sum_points, 70)

    def test_reigt_resalt_with_X(self):
        self.point_counter.game_resalt = 'XXXXX'
        self.point_counter.start_counter()
        self.assertEqual(self.point_counter.sum_points, 100)

    def test_reigt_resalt_with_slesh(self):
        self.point_counter.game_resalt = '1/-/3/5/'
        self.point_counter.start_counter()
        self.assertEqual(self.point_counter.sum_points, 60)

    def test_error_not_have_same_value(self):
        self.point_counter.game_resalt = 'X4/34X-/533--18'
        self.assertRaises(ValueError, self.point_counter.start_counter)

    def test_error_value_X(self):
        self.point_counter.game_resalt = '1X4/34-X'
        self.assertRaises(SyntaxError, self.point_counter.start_counter)

    def test_error_value_slesh(self):
        self.point_counter.game_resalt = 'X/434'
        self.assertRaises(SyntaxError, self.point_counter.start_counter)

    def test_type_error(self):
        self.point_counter.game_resalt = 'X4/a4'
        self.assertRaises(TypeError, self.point_counter.start_counter)

    def test_error_sum_big(self):
        self.point_counter.game_resalt = 'X4/34-81/87'
        self.assertRaises(SumError, self.point_counter.start_counter)


if __name__ == '__main__':
    unittest.main()
