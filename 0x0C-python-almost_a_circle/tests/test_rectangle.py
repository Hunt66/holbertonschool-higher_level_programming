#!/usr/bin/python3
"""Unittest for rectangle class
"""

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rec0 = Rectangle(5, 4)
        self.rec1 = Rectangle(2, 1)
        self.rec2 = Rectangle(3, 6, 0, 0, 13)
        self.rec3 = Rectangle(1, 2, 5, 6, 5)
        self.rec4 = Rectangle(1, 1, 1, 1, 32)
        self.rec5 = Rectangle(1, 1, 1, 1, 64)
        self.rec6 = Rectangle(2, 2, 2, 2, 128)
        self.rec7 = Rectangle(3, 3, 3, 3, 256)

    def test_to_dictionary(self):
        self.assertEqual(self.rec5.to_dictionary(),
                         {'x': 1, 'y': 1, 'width': 1, 'height': 1, 'id': 64})
        self.assertEqual(self.rec6.to_dictionary(),
                         {'x': 2, 'y': 2, 'width': 2, 'height': 2, 'id': 128})
        self.assertEqual(self.rec7.to_dictionary(),
                         {'x': 3, 'y': 3, 'width': 3, 'height': 3, 'id': 256})

    def test_id(self):
        self.assertEqual(self.rec0.id, 5)
        self.assertEqual(self.rec1.id, 6)
        self.assertEqual(self.rec2.id, 13)
        self.assertEqual(self.rec3.id, 5)

    def test_str(self):
        self.assertEqual(str(self.rec0), "[Rectangle] (7) 0/0 - 5/4")
        self.assertEqual(str(self.rec1), "[Rectangle] (8) 0/0 - 2/1")
        self.assertEqual(str(self.rec2), "[Rectangle] (13) 0/0 - 3/6")
        self.assertEqual(str(self.rec3), "[Rectangle] (5) 5/6 - 1/2")

    def test_update(self):
        self.rec4.update(89)
        self.assertEqual(str(self.rec4), "[Rectangle] (89) 1/1 - 1/1")
        self.rec4.update(89, 2)
        self.assertEqual(str(self.rec4), "[Rectangle] (89) 1/1 - 2/1")
        self.rec4.update(89, 2, 3)
        self.assertEqual(str(self.rec4), "[Rectangle] (89) 1/1 - 2/3")
        self.rec4.update(89, 2, 3, 4)
        self.assertEqual(str(self.rec4), "[Rectangle] (89) 4/1 - 2/3")
        self.rec4.update(89, 2, 3, 4, 5)
        self.assertEqual(str(self.rec4), "[Rectangle] (89) 4/5 - 2/3")
        self.rec4.update(1, 1, 1, 1, 1)
        self.rec4.update(height=2)
        self.assertEqual(str(self.rec4), "[Rectangle] (1) 1/1 - 1/2")
        self.rec4.update(width=2, x=2)
        self.assertEqual(str(self.rec4), "[Rectangle] (1) 2/1 - 2/2")
        self.rec4.update(x=3, height=3, y=3, width=3, id=89)
        self.assertEqual(str(self.rec4), "[Rectangle] (89) 3/3 - 3/3")

    def test_area(self):
        self.assertEqual(self.rec0.area(), 20)
        self.assertEqual(self.rec1.area(), 2)
        self.assertEqual(self.rec2.area(), 18)
        self.assertEqual(self.rec3.area(), 2)

    def test_width(self):
        self.assertEqual(self.rec0.width, 5)
        self.assertEqual(self.rec1.width, 2)
        self.assertEqual(self.rec2.width, 3)
        self.assertEqual(self.rec3.width, 1)

    def test_height(self):
        self.assertEqual(self.rec0.height, 4)
        self.assertEqual(self.rec1.height, 1)
        self.assertEqual(self.rec2.height, 6)
        self.assertEqual(self.rec3.height, 2)

    def test_x(self):
        self.assertEqual(self.rec0.x, 0)
        self.assertEqual(self.rec1.x, 0)
        self.assertEqual(self.rec2.x, 0)
        self.assertEqual(self.rec3.x, 5)

    def test_y(self):
        self.assertEqual(self.rec3.y, 6)
        self.assertEqual(self.rec0.y, 0)
        self.assertEqual(self.rec1.y, 0)
        self.assertEqual(self.rec2.y, 0)

class TestErrorRec(unittest.TestCase):

    def test_width_Type_error(self):
        self.assertRaises(TypeError, Rectangle, "1", 1, 1, 1, 1)
        self.assertRaises(TypeError, Rectangle, (1, 1), 1, 1, 1, 1)
        self.assertRaises(TypeError, Rectangle, {'1': 1}, 1, 1, 1, 1)
        self.assertRaises(TypeError, Rectangle, [1, 1], 1, 1, 1, 1)
        self.assertRaises(TypeError, Rectangle, float('nan'), 1, 1, 1, 1)
        self.assertRaises(TypeError, Rectangle, float('inf'), 1, 1, 1, 1)
        self.assertRaises(TypeError, Rectangle, 1.1, 1, 1, 1, 1)
        self.assertRaises(TypeError, Rectangle, False, 1, 1, 1, 1)
        self.assertRaises(TypeError, Rectangle, None, 1, 1, 1, 1)

    def test_height_Type_error(self):
        self.assertRaises(TypeError, Rectangle, 1, "1", 1, 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, (1, 1), 1, 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, {'1': 1}, 1, 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, [1, 1], 1, 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, float('nan'), 1, 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, float('inf'), 1, 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, 1.1, 1, 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, False, 1, 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, None, 1, 1, 1)

    def test_x_Type_error(self):
        self.assertRaises(TypeError, Rectangle, 1, 1, "1", 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, (1, 1), 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, {'1': 1}, 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, [1, 1], 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, float('nan'), 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, float('inf'), 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, 1.1, 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, False, 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, 1,  None, 1, 1)

    def test_y_Type_error(self):
        self.assertRaises(TypeError, Rectangle, 1, 1, 1, "1", 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, 1, (1, 1), 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, 1, {'1': 1}, 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, 1, [1, 1], 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, 1, float('nan'), 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, 1, float('inf'), 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, 1, 1.1, 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, 1, False, 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, 1,  None, 1)

    def test_width_Value_error(self):
        self.assertRaises(ValueError, Rectangle, -1, 1, 1, 1, 1)
        self.assertRaises(ValueError, Rectangle, 0, 1, 1, 1, 1)

    def test_height_Value_error(self):
        self.assertRaises(ValueError, Rectangle, 1, -1, 1, 1, 1)
        self.assertRaises(ValueError, Rectangle, 1, 0, 1, 1, 1)

    def test_x_Value_error(self):
        self.assertRaises(ValueError, Rectangle, 1, 1, -1, 1, 1)

    def test_y_Value_error(self):
        self.assertRaises(ValueError, Rectangle, 1, 1, 1, -1, 1)
