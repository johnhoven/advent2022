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
from day6p1 import day6p1
from day6p2 import day6p2
from day7p1 import day7p1
from day7p2 import day7p2
from day8p1 import day8p1
from day8p2 import day8p2
from day9p1 import day9p1
from day9p2 import day9p2
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

    def test_day6_part1_a(self):
        self.assertEqual(day6p1("day6asample.txt"), 7)

    def test_day6_part1_b(self):
        self.assertEqual(day6p1("day6bsample.txt"), 5)

    def test_day6_part1_c(self):
        self.assertEqual(day6p1("day6csample.txt"), 6)

    def test_day6_part1_d(self):
        self.assertEqual(day6p1("day6dsample.txt"), 10)

    def test_day6_part1_e(self):
        self.assertEqual(day6p1("day6esample.txt"), 11)

    def test_day6_part2_a(self):
        self.assertEqual(day6p2("day6asample.txt"), 19)

    def test_day6_part2_b(self):
        self.assertEqual(day6p2("day6bsample.txt"), 23)

    def test_day6_part2_c(self):
        self.assertEqual(day6p2("day6csample.txt"), 23)

    def test_day6_part2_d(self):
        self.assertEqual(day6p2("day6dsample.txt"), 29)

    def test_day6_part2_e(self):
        self.assertEqual(day6p2("day6esample.txt"), 26)

    def test_day7_part1(self):
        self.assertEqual(day7p1("day7asample.txt"), 95437)

    def test_day7_part2(self):
        self.assertEqual(day7p2("day7asample.txt"), 24933642)

    def test_day8_part1(self):
        self.assertEqual(day8p1("day8asample.txt"), 21)

    def test_day8_part2(self):
        self.assertEqual(day8p2("day8asample.txt"), 8)

    def test_day9_part1(self):
        self.assertEqual(day9p1("day9asample.txt"), 13)

    def test_day9_part2(self):
        self.assertEqual(day9p2("day9asample.txt"), 1)

    def test_day9_part2_b(self):
        self.assertEqual(day9p2("day9bsample.txt"), 36)


if __name__ == '__main__':
    unittest.main()
