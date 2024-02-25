#!/usr/bin/python3
'''Module for Rectangle unit tests.'''

import unittest
from models.rectangle import Rectangle
from models.base import Base
from unittest.mock import patch
import io

class TestRectangle(unittest.TestCase):
    def test_constructor(self):
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)

    def test_constructor_with_id(self):
        rectangle = Rectangle(5, 10, 1, 2, 10)
        self.assertEqual(rectangle.id, 10)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 1)
        self.assertEqual(rectangle.y, 2)

    def test_width_property(self):
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.width, 5)

    def test_width_setter(self):
        rectangle = Rectangle(5, 10)
        rectangle.width = 15
        self.assertEqual(rectangle.width, 15)

    def test_invalid_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-5, 10)

    def test_invalid_width_type(self):
        with self.assertRaises(TypeError):
            Rectangle("5", 10)

    def test_height_property(self):
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.height, 10)

    def test_height_setter(self):
        rectangle = Rectangle(5, 10)
        rectangle.height = 15
        self.assertEqual(rectangle.height, 15)

    def test_invalid_height(self):
        with self.assertRaises(ValueError):
            Rectangle(5, -10)

    def test_invalid_height_type(self):
        with self.assertRaises(TypeError):
            Rectangle(5, "10")

    def test_x_property(self):
        rectangle = Rectangle(5, 10, 2)
        self.assertEqual(rectangle.x, 2)

    def test_x_setter(self):
        rectangle = Rectangle(5, 10, 2)
        rectangle.x = 5
        self.assertEqual(rectangle.x, 5)

    def test_invalid_x(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 10, "2")

    def test_y_property(self):
        rectangle = Rectangle(5, 10, 2, 3)
        self.assertEqual(rectangle.y, 3)

    def test_y_setter(self):
        rectangle = Rectangle(5, 10, 2, 3)
        rectangle.y = 6
        self.assertEqual(rectangle.y, 6)

    def test_invalid_y(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 10, 2, "3")

    def test_area(self):
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.area(), 50)

    def test_display(self):
        rectangle = Rectangle(2, 3, 1, 1)
        expected_output = " #\n #\n #\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            rectangle.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_str(self):
        rectangle = Rectangle(5, 10, 1, 2, 10)
        self.assertEqual(str(rectangle), "[Rectangle] (10) 1/2 - 5/10")

    def test_update(self):
        rectangle = Rectangle(5, 10, 1, 2, 10)
        rectangle.update(20, 7, 8, 9, 10)
        self.assertEqual(rectangle.id, 20)
        self.assertEqual(rectangle.width, 7)
        self.assertEqual(rectangle.height, 8)
        self.assertEqual(rectangle.x, 9)
        self.assertEqual(rectangle.y, 10)

    def test_to_dictionary(self):
        rectangle = Rectangle(5, 10, 1, 2, 10)
        expected_dict = {'id': 10, 'width': 5, 'height': 10, 'x': 1, 'y': 2}
        self.assertEqual(rectangle.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
