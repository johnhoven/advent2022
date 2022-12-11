from day1a import day1
from day1b import day1part2
from day2p1 import day2p1
from day2p2 import day2p2
from day3p1 import day3p1
from day3p2 import day3p2
from day4p1 import day4p1
from day4p2 import day4p2
from day5p1 import day5p1
from day5p2 import day5p2
import unittest


class Advent2022Tests(unittest.TestCase):
    def test_day1_part1(self):
        self.assertEqual(day1("day1asample.txt"), 24000)

    def test_day1_part2(self):
        self.assertEqual(day1part2("day1asample.txt"), 45000)

    def test_day2_part1(self):
        self.assertEqual(day2p1("day2asample.txt"), 15)

    def test_day2_part2(self):
        self.assertEqual(day2p2("day2asample.txt"), 12)

    def test_day3_part1(self):
        self.assertEqual(day3p1("day3asample.txt"), 157)

    def test_day3_part2(self):
        self.assertEqual(day3p2("day3asample.txt"), 70)

    def test_day4_part1(self):
        self.assertEqual(day4p1("day4asample.txt"), 2)

    def test_day4_part2(self):
        self.assertEqual(day4p2("day4asample.txt"), 4)

    def test_day5_part1(self):
        self.assertEqual(day5p1("day5asample.txt"), "CMZ")

    def test_day5_part2(self):
        self.assertEqual(day5p2("day5asample.txt"), "MCD")


if __name__ == '__main__':
    unittest.main()
