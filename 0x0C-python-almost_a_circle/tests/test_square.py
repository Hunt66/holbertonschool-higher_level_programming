#!/usr/bin/python3
"""Unittest for square class
"""

import unittest
import sys
import io
from contextlib import contextmanager
from models.square import Square
from models.base import Base

@contextmanager
def cap_out():
    nout = io.StringIO()
    nerr =  io.StringIO()
    oout = sys.stdout
    oerr = sys.stderr
    try:
        sys.stdout = nout
        sys.stderr = nerr
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout = oout
        sys.stderr = oerr

class TestSquare(unittest.TestCase):

    def setUp(self):
        self.rec0 = Square(5)
        self.rec1 = Square(2)
        self.rec2 = Square(6, 0, 0, 13)
        self.rec3 = Square(2, 5, 6, 5)
        self.rec4 = Square(1, 1, 1, 32)
        self.rec5 = Square(1, 1, 1, 64)
        self.rec6 = Square(2, 2, 2, 128)
        self.rec7 = Square(3, 3, 3, 256)

    def test_display(self):
        with cap_out() as (out, err):
            self.rec0.display()
            buf = out.getvalue()
            self.assertEqual(buf, '#####\n' * 5)
        with cap_out() as (out, err):
            self.rec1.display()
            buf = out.getvalue()
            self.assertEqual(buf, '##\n' * 2)
        with cap_out() as (out, err):
            self.rec3.display()
            buf = out.getvalue()
            self.assertEqual(buf, ('\n' * 6) + ('     ##\n' * 2))

    def test_to_dictionary(self):
        self.assertEqual(self.rec5.to_dictionary(),
                         {'x': 1, 'y': 1, 'size': 1, 'id': 64})
        self.assertEqual(self.rec6.to_dictionary(),
                         {'x': 2, 'y': 2, 'size': 2, 'id': 128})
        self.assertEqual(self.rec7.to_dictionary(),
                         {'x': 3, 'y': 3, 'size': 3, 'id': 256})

    def test_id(self):
        self.assertEqual(self.rec0.id, 5)
        self.assertEqual(self.rec1.id, 6)
        self.assertEqual(self.rec2.id, 13)
        self.assertEqual(self.rec3.id, 5)

    def test_str(self):
        self.assertEqual(str(self.rec0), "[Square] (9) 0/0 - 5")
        self.assertEqual(str(self.rec1), "[Square] (10) 0/0 - 2")
        self.assertEqual(str(self.rec2), "[Square] (13) 0/0 - 6")
        self.assertEqual(str(self.rec3), "[Square] (5) 5/6 - 2")

    def test_update(self):
        self.rec4.update(89)
        self.assertEqual(str(self.rec4), "[Square] (89) 1/1 - 1")
        self.rec4.update(89, 2)
        self.assertEqual(str(self.rec4), "[Square] (89) 1/1 - 2")
        self.rec4.update(89, 2, 3)
        self.assertEqual(str(self.rec4), "[Square] (89) 3/1 - 2")
        self.rec4.update(89, 2, 3, 4)
        self.assertEqual(str(self.rec4), "[Square] (89) 3/4 - 2")
        self.rec4.update(1, 1, 1, 1)
        self.rec4.update(size=2)
        self.assertEqual(str(self.rec4), "[Square] (1) 1/1 - 2")
        self.rec4.update(size=4, x=2)
        self.assertEqual(str(self.rec4), "[Square] (1) 2/1 - 4")
        self.rec4.update(x=3, size=3, y=3, id=89)
        self.assertEqual(str(self.rec4), "[Square] (89) 3/3 - 3")

    def test_area(self):
        self.assertEqual(self.rec0.area(), 25)
        self.assertEqual(self.rec1.area(), 4)
        self.assertEqual(self.rec2.area(), 36)
        self.assertEqual(self.rec3.area(), 4)

    def test_size(self):
        self.assertEqual(self.rec0.size, 5)
        self.assertEqual(self.rec1.size, 2)
        self.assertEqual(self.rec2.size, 6)
        self.assertEqual(self.rec3.size, 2)

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

class TestErrorSq(unittest.TestCase):

    def test_size_Type_error(self):
        self.assertRaises(TypeError, Square, "1", 1, 1, 1)
        self.assertRaises(TypeError, Square, (1, 1), 1, 1, 1)
        self.assertRaises(TypeError, Square, {'1': 1}, 1, 1, 1)
        self.assertRaises(TypeError, Square, [1, 1], 1, 1, 1)
        self.assertRaises(TypeError, Square, float('nan'), 1, 1, 1)
        self.assertRaises(TypeError, Square, float('inf'), 1, 1, 1)
        self.assertRaises(TypeError, Square, 1.1, 1, 1, 1)
        self.assertRaises(TypeError, Square, False, 1, 1, 1)
        self.assertRaises(TypeError, Square, None, 1, 1, 1)

    def test_x_Type_error(self):
        self.assertRaises(TypeError, Square, 1, "1", 1, 1)
        self.assertRaises(TypeError, Square, 1, (1, 1), 1, 1)
        self.assertRaises(TypeError, Square, 1, {'1': 1}, 1, 1)
        self.assertRaises(TypeError, Square, 1, [1, 1], 1, 1)
        self.assertRaises(TypeError, Square, 1, float('nan'), 1, 1)
        self.assertRaises(TypeError, Square, 1, float('inf'), 1, 1)
        self.assertRaises(TypeError, Square, 1, 1.1, 1, 1)
        self.assertRaises(TypeError, Square, 1, False, 1, 1)
        self.assertRaises(TypeError, Square, 1, None, 1, 1)

    def test_y_Type_error(self):
        self.assertRaises(TypeError, Square, 1, 1, "1", 1)
        self.assertRaises(TypeError, Square, 1, 1, (1, 1), 1)
        self.assertRaises(TypeError, Square, 1, 1, {'1': 1}, 1)
        self.assertRaises(TypeError, Square, 1, 1, [1, 1], 1)
        self.assertRaises(TypeError, Square, 1, 1, float('nan'), 1)
        self.assertRaises(TypeError, Square, 1, 1, float('inf'), 1)
        self.assertRaises(TypeError, Square, 1, 1, 1.1, 1)
        self.assertRaises(TypeError, Square, 1, 1, False, 1)
        self.assertRaises(TypeError, Square, 1, 1,  None, 1)

    def test_size_Value_error(self):
        self.assertRaises(ValueError, Square, -1, 1, 1, 1)
        self.assertRaises(ValueError, Square, 0, 1, 1, 1)

    def test_x_Value_error(self):
        self.assertRaises(ValueError, Square, 1, -1, 1, 1)

    def test_y_Value_error(self):
        self.assertRaises(ValueError, Square, 1, 1, -1, 1)
