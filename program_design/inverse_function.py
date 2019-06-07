# --------------
# User Instructions
#
# Write a function, inverse, which takes as input a monotonically
# increasing (always increasing) function that is defined on the
# non-negative numbers. The runtime of your program should be
# proportional to the LOGARITHM of the input. You may want to
# do some research into binary search and Newton's method to
# help you out.
#
# This function should return another function which computes the
# inverse of the input function.
#
# Your inverse function should also take an optional parameter,
# delta, as input so that the computed value of the inverse will
# be within delta of the true value.

# -------------
# Grading Notes
#
# Your function will be called with three test cases. The
# input numbers will be large enough that your submission
# will only terminate in the allotted time if it is
# efficient enough.


import time
import timeit
import cProfile

def debugger(f):
    def _f(*args):
        print(args, f.p)
        f.p += 1
        return f(*args)
    f.p = 0
    return _f


def timer(f):
    def _f(args):
        s = time.time()
        result = [f(args)]*10
        e = time.time()
        print('%s, time:%s'%(f.__name__,s-e))
        result = f(args)
        return result
    return _f

def slow_inverse(f, delta=1/1024.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def f_1(y):
        x = 0
        while f(x) < y:
            x += delta
        # Now x is too big, x-delta is too small; pick the closest to y
        return x if (f(x)-y < y-f(x-delta)) else x-delta
    return f_1

@timer
def my_inverse(f, delta=1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def _f(y):
        x = 1
        while f(x) < y:
            x *= 2
        left = 0 if x == 1 else x/2.
        return binary_search(f, y, left, x, delta)
    return _f

@timer
def inverse(f, delta=1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def _f(y):
        x = 1
        while f(x) < y:
            x *= 2
        left = 0 if x == 1 else x/2.
        return binary_search_solution(f, y, left, x, delta)
    return _f


def binary_search(f, y, left, right, delta):
    while right - left >= delta:
        m = (left + right) / 2.
        if f(m) < y:
            left = m + delta
        else:
            right = m - delta
    return m


def binary_search_solution(f, y, lo, hi, delta):
    while lo <= hi:
        x = (lo + hi) / 2.
        if f(x) < y:
            lo = x + delta
        elif f(x) > y:
            hi = x - delta
        else:
            return x
    return hi if (f(hi) - y < y - f(lo)) else lo

def square(x):
    return x*x


def power10(x):
    return 10**x


fastlog10 = inverse(power10)
mylog10 = my_inverse(power10)

sqrt = inverse(square)
mysqrt = my_inverse(square)
print(sqrt(16), mysqrt(16))
print(fastlog10(12340000), mylog10(12340000))
cProfile.run('sqrt(10e10)')
cProfile.run('mysqrt(10e10)')
cProfile.run('fastlog10(12340000)')
cProfile.run('mylog10(12340000)')
