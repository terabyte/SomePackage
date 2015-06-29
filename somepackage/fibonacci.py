''' impl for class Fibonacci '''

#pylint: disable=R0903,R0201

class Fibonacci(object):
    ''' this module provides a method for calculating fibbonacci numbers in
    amortized linear time '''

    def __init__(self):
        pass

    @_memoize
    def fib(self, num):
        ''' returns the num-th fibonacci number '''
        if num < 1:
            return 0
        if num < 3:
            return 1
        return self.fib(num-1) + self.fib(num-2)

    def _memoize(self, func):
        ''' memoize a function '''
        memo = {}
        def helper(arg):
            ''' helper '''
            if arg not in memo:
                memo[arg] = func(arg)
            return memo[arg]
        return helper

