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



def slow_inverse(f, delta=1/128.):
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


def inverse(f, delta=1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def _f(y):
        x = 1
        while f(x) < y:
            x *= 2
        left = 0 if x == 1 else x/2
        return binary_search(f, y, left, x, delta)
    return _f

def binary_search(f, y, left, right, delta):
    while abs(right - left) >= delta:
        m = (left + right) / 2
        if f(m) > y:
            right = m
        elif f(m) < y:
            left = m
        else:
            return m
    return m

def square(x):
    return x*x


def power10(x):
    return 10**x


fastlog10 = inverse(power10)


sqrt = inverse(square)
print(sqrt(100))
print(fastlog10(12340000))
