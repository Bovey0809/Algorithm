null = frozenset()


def match(pattern, text):
    '''return the longest first matches text'''
    remainders = pattern(text)
    if remainders:
        shorteset = min(remainders, key=len)
        return text[:len(text)-len(shorteset)]


def lit(s):
    '''return the reminded text if the text start with s'''
    return lambda text: set(text[1:]) if text.startswith(s) else null


def seq(x, y):
    '''return text suits for pattern x and pattern y
    x: pattern
    y: pattern
    trick: suits pattern x and then use the reminded to suits y
    '''

    return lambda text: set().union(*map(y, x(text)))


def alt(x, y):
    '''return text matches x or y'''
    return lambda text: x(text) | y(text)


def oneof(chars):
    '''if text start one of the char in the chars, return reminds'''
    return lambda t: set(t[1:]) if (t and t[0] in chars) else null


def dot(t): return set(t[1:]) if t else null


def eol(t): return set('') if t == '' else null


def star(x):
    '''repeat using pattern x to the text until it exhausted'''
    return lambda t: ((set(t)) |
                      set(t2) for t1 in x(t) if t1 != t
                      for t2 in star(x)(t1))
