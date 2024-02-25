#!/usr/bin/python3

'''Module for Square unit tests.'''
import unittest
from models.base import Base
from models.square import Square
from unittest.mock import patch
import io


class TestSquare(unittest.TestCase):
    def test_constructor(self):
        square = Square(5)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

    def test_constructor_with_id(self):
        square = Square(5, 1, 2, 10)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)

    def test_size_property(self):
        square = Square(5)
        self.assertEqual(square.size, 5)

    def test_size_setter(self):
        square = Square(5)
        square.size = 10
        self.assertEqual(square.size, 10)

    def test_invalid_size(self):
        with self.assertRaises(ValueError):
            Square(-5)

    def test_invalid_size_type(self):
        with self.assertRaises(TypeError):
            Square("5")

    def test_x_property(self):
        square = Square(5, 2)
        self.assertEqual(square.x, 2)

    def test_x_setter(self):
        square = Square(5, 2)
        square.x = 5
        self.assertEqual(square.x, 5)

    def test_invalid_x(self):
        with self.assertRaises(TypeError):
            Square(5, "2")

    def test_y_property(self):
        square = Square(5, 2, 3)
        self.assertEqual(square.y, 3)

    def test_y_setter(self):
        square = Square(5, 2, 3)
        square.y = 6
        self.assertEqual(square.y, 6)

    def test_invalid_y(self):
        with self.assertRaises(TypeError):
            Square(5, 2, "3")

    def test_area(self):
        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_str(self):
        square = Square(5, 1, 2, 10)
        self.assertEqual(str(square), "[Square] (10) 1/2 - 5")

    def test_update(self):
        square = Square(5, 1, 2, 10)
        square.update(20, 7, 8, 9)
        self.assertEqual(square.id, 20)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 8)
        self.assertEqual(square.y, 9)

    def test_to_dictionary(self):
        square = Square(5, 1, 2, 10)
        expected_dict = {'id': 10, 'size': 5, 'x': 1, 'y': 2}
        self.assertEqual(square.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()

