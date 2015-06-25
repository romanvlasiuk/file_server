import unittest
from file_server.main import max_value

class TestMax(unittest.TestCase):

    def test_max_value(self):
        self.assertEqual(max_value(1, 2), 2)

if __name__ == '__main__':
    unittest.main()
