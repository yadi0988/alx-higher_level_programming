from models.base import Base
import unittest


class test_id(unittest.TestCase):

    def test_Base(self):
        obj = Base()
        obj2 = Base()
        obj3 = Base()
        obj4 = Base(12)
        obj5 = Base()
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 3)
        self.assertEqual(obj4.id, 12)
        self.assertEqual(obj5.id, 4)
