import unittest
from Main import Main

class TestUnit(unittest.TestCase):
    def test_add(self):
        f = Main()
        self.assertEqual(f.func(1),2)
        self.assertEqual(f.func(-1),0)
        self.assertEqual(f.func(3),4)

if __name__ == '__main__':
    unittest.main()
