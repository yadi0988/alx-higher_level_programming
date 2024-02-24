from models.base import Base
import unittest


class test_id(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_id_assignment(self):
        test_cases = [
            (None, 1),
            (None, 2),
            (None, 3),
            (12, 12)
        ]
        for value, expected in test_cases:
            self.test_id(value, expected)

    def test_id(self, input_value=1, expected_id=1):
        obj = Base(input_value)
        self.assertEqual(obj.id, expected_id)
