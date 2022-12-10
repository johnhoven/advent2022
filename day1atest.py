from day1a import day1
import unittest


class Day1Test(unittest.TestCase):
    def test_day1(self):
        self.assertEqual(day1("day1asample.txt"), 24000)


if __name__ == '__main__':
    unittest.main()
