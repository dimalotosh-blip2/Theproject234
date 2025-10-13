import logging
import unittest
from Lesson_8 import *

logging.basicConfig(
    filename="test_log.txt",
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

class TestCalculator(unittest.TestCase):
    def test_sum_numbers(self):
        self.assertEqual(sum_numbers(2, 3, 5), 10)

    def test_sum_with_kwargs(self):
        self.assertEqual(sum_numbers(x=4, y=6), 10)
        self.assertEqual(sum_numbers(1, 2, x=3), 6)

if __name__ == "__main__":
    logging.info(unittest.main())
    logging.info("Testing finished")
