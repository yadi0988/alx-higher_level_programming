from models.base import Base
import unittest


class test_id(unittest.TestCase):

    def test_no_arg(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, obj2.id - 1)

    def test_scope(self):
        obj1 = Base(12)
        obj1.id = 2
        self.assertEqual(obj1.id, 2)

    def test_many_id(self):
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        self.assertEqual(obj1.id, obj3.id - 2)

    def test_None_arg(self):
        obj1 = Base(None)
        obj2 = Base(None)
        self.assertEqual(obj1.id, obj2.id - 1)

    def test_with_arg(self):
        obj1 = Base(12)
        self.assertEqual(obj1.id, 12)

    def test_mix(self):
        obj1 = Base()
        obj2 = Base(12)
        obj3 = Base()
        self.assertEqual(obj1.id, obj3.id - 1)
