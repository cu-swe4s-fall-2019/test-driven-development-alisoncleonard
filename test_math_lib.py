"""
Unit test file for math_lib.py, a library of math functions
"""

import unittest
import math_lib
import random
import statistics
import math


class TestMathLib(unittest.TestCase):
    def test_list_mean_none_list(self):
        self.assertEqual(math_lib.list_mean(None), None)

    def test_list_mean_empty_list(self):
        self.assertEqual(math_lib.list_mean([]), None)

    def test_list_stdev_none_list(self):
        self.assertEqual(math_lib.list_stdev(None), None)

    def test_list_stdev_empty_list(self):
        self.assertEqual(math_lib.list_stdev([]), None)

    def test_list_mean_constant(self):
        m = math_lib.list_mean([3, 4, 5])
        self.assertEqual(m, 4.0)

    def test_list_stdev_constant(self):
        s = math_lib.list_stdev([3, 4, 5])
        self.assertTrue(math.isclose(s, statistics.pstdev([3, 4, 5])))

    def test_list_mean_random_ints(self):
        for i in range(100):
            L = []
            for j in range(10):
                L.append(random.randint(0, 100))
            r = math_lib.list_mean(L)
            e = statistics.mean(L)
            self.assertTrue(math.isclose(r, e))

    def test_list_stdev_random_ints(self):
        for i in range(100):
            L = []
            for j in range(10):
                L.append(random.randint(0, 100))
            v = math_lib.list_stdev(L)
            w = statistics.pstdev(L)
            self.assertTrue(math.isclose(v, w))

    def test_list_mean_random_floats(self):
        for i in range(100):
            L = []
            for j in range(10):
                L.append(random.uniform(0, 100))
            r = math_lib.list_mean(L)
            e = statistics.mean(L)
            self.assertTrue(math.isclose(r, e))

    def test_list_stdev_random_floats(self):
        for i in range(100):
            L = []
            for j in range(10):
                L.append(random.uniform(0, 100))
            v = math_lib.list_stdev(L)
            w = statistics.pstdev(L)
            self.assertTrue(math.isclose(v, w))

    def test_list_mean_non_int_or_float(self):
        L = []
        for i in range(10):
            L.append(random.randint(0, 100))
        L.append('X')
        for j in range(10):
            L.append(random.uniform(0, 100))

        with self.assertRaises(ValueError) as ex:
            math_lib.list_mean(L)
        message = 'Unsupported value. List of ints and floats only'
        self.assertEqual(str(ex.exception), message)

    def test_list_mean_not_a_list(self):
        with self.assertRaises(TypeError) as ex:
            math_lib.list_mean(random.randint(0, 100))
        message = 'Unsupported data type. Must pass a list'
        self.assertEqual(str(ex.exception), message)

    def test_list_stdev_non_int_or_float(self):
        L = []
        for i in range(10):
            L.append(random.randint(0, 100))
        L.append('X')
        for j in range(10):
            L.append(random.uniform(0, 100))

        with self.assertRaises(ValueError) as ex:
            math_lib.list_stdev(L)
        message = 'Unsupported value. List of ints and floats only'
        self.assertEqual(str(ex.exception), message)

    def test_list_stdev_not_a_list(self):
        with self.assertRaises(TypeError) as ex:
            math_lib.list_mean(random.randint(0, 100))
        message = 'Unsupported data type. Must pass a list'
        self.assertEqual(str(ex.exception), message)


if __name__ == '__main__':
    unittest.main()
