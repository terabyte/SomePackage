#!/usr/bin/env python2.7
''' test for fibonacci module '''
import unittest

from somepackage.fibonacci import Fibonacci

# pylint: disable=C0111,R0904
class FibonacciTest(unittest.TestCase):

    def test_neg_number(self):
        fib = Fibonacci()
        self.assertEqual(0, fib.fib(-5))


    def test_zero(self):
        fib = Fibonacci()
        self.assertEqual(0, fib.fib(0))

    def test_one(self):
        fib = Fibonacci()
        self.assertEqual(1, fib.fib(1))

    def test_two(self):
        fib = Fibonacci()
        self.assertEqual(1, fib.fib(2))

    def test_to_ten(self):
        fib = Fibonacci()
        self.assertEqual(2, fib.fib(3))
        self.assertEqual(3, fib.fib(4))
        self.assertEqual(5, fib.fib(5))
        self.assertEqual(8, fib.fib(6))
        self.assertEqual(13, fib.fib(7))
        self.assertEqual(21, fib.fib(8))
        self.assertEqual(34, fib.fib(9))
        self.assertEqual(55, fib.fib(10))

    def test_larger_nums(self):
        fib = Fibonacci()
        self.assertEqual(55, fib.fib(20))
        self.assertEqual(55, fib.fib(40))

