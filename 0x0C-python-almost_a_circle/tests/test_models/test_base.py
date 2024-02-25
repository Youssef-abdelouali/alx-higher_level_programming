#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def test_constructor(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_constructor_with_id(self):
        base = Base(10)
        self.assertEqual(base.id, 10)

    def test_to_json_string(self):
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

        json_string = Base.to_json_string([{'id': 1, 'name': 'object1'}, {'id': 2, 'name': 'object2'}])
        self.assertEqual(json_string, '[{"id": 1, "name": "object1"}, {"id": 2, "name": "object2"}]')

    def test_from_json_string(self):
        objects = Base.from_json_string("[]")
        self.assertEqual(objects, [])

        objects = Base.from_json_string('[{"id": 1, "name": "object1"}, {"id": 2, "name": "object2"}]')
        self.assertEqual(objects, [{'id': 1, 'name': 'object1'}, {'id': 2, 'name': 'object2'}])

    def test_create(self):
        obj = Base.create(id=1, name='object1')
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.name, 'object1')

    def test_fieldnames(self):
        fieldnames = Base.fieldnames()
        self.assertEqual(fieldnames, ['id'])


if __name__ == '__main__':
    unittest.main()

