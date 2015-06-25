import unittest
import StringIO
from file_server.main import max_value, fr_dictionary


class TestMax(unittest.TestCase):

    def test_max_value(self):
        self.assertEqual(max_value(1, 2), 2)

    def test_fr_dict(self):
        s = StringIO.StringIO('a b a b a')
        self.assertEqual(fr_dictionary(s, open=lambda s, m: s), {'a': 3, 'b': 2})

if __name__ == '__main__':
    unittest.main()


