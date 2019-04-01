# --------------
# User Instructions
#
# Complete the code for the compiler by completing the constructor
# for the patterns alt(x, y) and oneof(chars).

from functools import update_wrapper

null = frozenset([])


def lit(s):
    set_s = set([s])
    return lambda Ns: set_s if len(s) in Ns else null


def alt(x, y): return lambda Ns: x(Ns) | y(Ns)


def star(x): return lambda Ns: opt(plus(x))(Ns)


def plus(x): return lambda Ns: genseq(x, star(x), Ns, startx=1)  # Tricky


def oneof(chars):
    set_chars = set(chars)
    return lambda Ns: set_chars if 1 in Ns else null


def seq(x, y): return lambda Ns: genseq(x, y, Ns)


def opt(x): return alt(epsilon, x)


dot = oneof('?')    # You could expand the alphabet to more chars.
epsilon = lit('')   # The pattern that matches the empty string.


def genseq(x, y, Ns, startx=0):
    if not Ns:
        return null
    xmatches = x(set(range(startx, max(Ns) + 1)))
    Ns_x = set(len(m) for m in xmatches)
    Ns_y = set(n-m for n in Ns for m in Ns_x if n-m >= 0)
    ymatches = y(Ns_y)
    return set(m1 + m2
               for m1 in xmatches for m2 in ymatches
               if len(m1+m2) in Ns)


def decorator(d):
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d


@decorator
def n_arg(f):
    '''funtion to turn f(x, y) -> f(x, *args)'''
    def n_arg_f(x, *args):
        '''helper function in n_arg'''
        if not args:
            return x
        return f(x, n_arg_f(*args))
    update_wrapper(n_arg, f)
    return n_arg_f


def test():

    f = lit('hello')
    assert f(set([1, 2, 3, 4, 5])) == set(['hello'])
    assert f(set([1, 2, 3, 4])) == null

    g = alt(lit('hi'), lit('bye'))
    assert g(set([1, 2, 3, 4, 5, 6])) == set(['bye', 'hi'])
    assert g(set([1, 3, 5])) == set(['bye'])

    h = oneof('theseletters')
    assert h(set([1, 2, 3])) == set(['t', 'h', 'e', 's', 'l', 'r'])
    assert h(set([2, 3, 4])) == null

    def addxy(x, y):
        "This is the function addxy document"
        return x+y
    k = n_arg(addxy)
    assert k(1, 2, 3) == 6
    assert k(1, 2) == 3
    assert k(1) == 1

    print(help(addxy))

    @n_arg
    def addxy(x, y):
        '''This is under @'''
        return x+y
    assert addxy(1, 2, 3) == 6
    print(help(addxy))
    return 'tests pass'


print(test())
