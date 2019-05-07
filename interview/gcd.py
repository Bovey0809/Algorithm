from itertools import combinations, accumulate
from math import gcd

lcm_d = {}


def printlcm(f):
    def _f(*args):
        output = f(*args)
        lcm_d['args'] = output
        print(f(*args))
        return output
    return _f


def lcm(*args):
    """
    >>> lcm(1, 2)
    2
    >>> lcm(2, 4)
    4
    >>> lcm(0, 4)
    0
    >>> lcm(1, 2, 3)
    6
    >>> lcm(2, 3, 4)
    12
    >>> lcm(1, 2, 3, 5)
    30
    >>> lcm(2, 3, 4, 5)
    60
    """
    if len(args) == 1:
        return args
    a, b = args[:2]
    if len(args) == 2:
        return (a // gcd(a, b) * b)
    return lcm(lcm(a, b), *args[2:])


def n_gcd(l, r, n):
    '''
    Return the number of gcd(n) in [l, r]

    >>> n_gcd(1, 10, 2)
    5
    >>> n_gcd(1, 10, 3)
    3
    >>> n_gcd(2, 10, 4)
    2
    >>> n_gcd(1, 100, 1)
    100
    >>> n_gcd(1, 100, 2)
    50
    >>> n_gcd(2, 100, 4)
    25
    '''
    output = r // n - (l // n)
    return output + 1 if l == n else output


def n_gcd_for_list(l, r, m, args):
    """                                                         
    >>> n_gcd_for_list(1, 10, 3, [2, 3, 4])
    3
    >>> n_gcd_for_list(1, 10, 4, [2, 3, 4, 5])                         
    2
    >>> n_gcd_for_list(1, 10, 3, [1, 3, 4])                            
    0
    >>> n_gcd_for_list(2, 100, 2, [2, 4])
    49
    """
    length = r - l + 1
    for i in args:
        length -= n_gcd(l, r, i)
    for n in range(2, m+1):
        for m in combinations(args, n):
            if n % 2 == 0:
                length += n_gcd(l, r, lcm(*m))
            else:
                length -= n_gcd(l, r, lcm(*m))
    return int(length)


print(n_gcd_for_list(1, 1000000000000000000,
                     10, [48, 84, 96, 56, 99, 5, 66, 31]))
