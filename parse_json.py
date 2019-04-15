from functools import update_wrapper
# from string import split
import re

def grammar(description, whitespace=r'\s*'):
    G = {' ': whitespace}
    description = description.replace('\t', ' ') # no tabs!
    for line in str.split(description, '\n'):
        lhs, rhs = str.split(line, ' => ', 1)
        alternatives = str.split(rhs, ' | ')
        G[lhs] = tuple(map(str.split, alternatives))
    return G

def decorator(d):
    "Make function d a decorator: d wraps a function fn."
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

@decorator
def disable(f):
    def _f(d):
        return d
    return _f

@decorator
def memo(f):
    """Decorator that caches the return value for each call to f(args).
    Then when called again with same args, we can just look it up."""
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            # some element of args can't be a dict key
            return f(args)
    return _f


@disable
@decorator
def debugger(f):
    def _f(*args):
        print(f.__name__, args)
        return f(*args)
    return _f




@debugger
def parse(start_symbol, text, grammar):
    """Example call: parse('Exp', '3*x + b', G).
    Returns a (tree, remainder) pair. If remainder is '', it parsed the whole
    string. Failure iff remainder is None. This is a deterministic PEG parser,
    so rule order (left-to-right) matters. Do 'E => T op E | T', putting the
    longest parse first; don't do 'E => T | T op E'
    Also, no left recursion allowed: don't do 'E => E op T'"""

    tokenizer = grammar[' '] + '(%s)'
    @debugger
    def parse_sequence(sequence, text):
        result = []
        for atom in sequence:
            tree, text = parse_atom(atom, text)
            if text is None: return Fail
            result.append(tree)
        return result, text

    @debugger
    def parse_atom(atom, text):
        if atom in grammar:  # Non-Terminal: tuple of alternatives
            for alternative in grammar[atom]:
                tree, rem = parse_sequence(alternative, text)
                if rem is not None: return [atom]+tree, rem
            return Fail
        else:  # Terminal: match characters against start of text
            m = re.match(tokenizer % atom, text)
            return Fail if (not m) else (m.group(1), text[m.end():])
    # Body of parse:
    return parse_atom(start_symbol, text)

Fail = (None, None)

JSON_solution = grammar("""object => { } | { members }
members => pair , members | pair
pair => string : value
array => [[] []] | [[] elements []]
elements => value , elements | value
value => string | number | object | array | true | false | null
string => "[^"]*"
number => int frac exp | int frac | int exp | int
int => -?[1-9][0-9]*
frac => [.][0-9]+
exp => [eE][-+]?[0-9]+""", whitespace='\s*')


# 这里有几点要要注意, 主要是影响了re的语法.
# 1. string
# 2. array里面的[]中括号, 和re里面的中括号冲突.
JSON = grammar("""object => { members } | { }
members => pair , members | pair
pair => string : value
string => "[^"]*"
value => string | number | object | array | true | false | null
number => int frac exp | int frac | int exp | int
int => -?[1-9]\d*
frac => \.\d+
exp => [Ee][-+]?\d+
array => [[] []] | [[] elements []]
elements => value , elements | value""")

def json_parse(text):
    return parse('value', text, JSON)

def test():
    assert json_parse('["testing", 1, 2, 3]') == (
                       ['value', ['array', '[', ['elements', ['value',
                       ['string', '"testing"']], ',', ['elements', ['value', ['number',
                       ['int', '1']]], ',', ['elements', ['value', ['number',
                       ['int', '2']]], ',', ['elements', ['value', ['number',
                       ['int', '3']]]]]]], ']']], '')

    assert json_parse('-123.456e+789') == (
                       ['value', ['number', ['int', '-123'], ['frac', '.456'], ['exp', 'e+789']]], '')

    assert json_parse('{"age": 21, "state":"CO","occupation":"rides the rodeo"}') == (
                      ['value', ['object', '{', ['members', ['pair', ['string', '"age"'],
                       ':', ['value', ['number', ['int', '21']]]], ',', ['members',
                      ['pair', ['string', '"state"'], ':', ['value', ['string', '"CO"']]],
                      ',', ['members', ['pair', ['string', '"occupation"'], ':',
                      ['value', ['string', '"rides the rodeo"']]]]]], '}']], '')
    return 'tests pass'

print(test())
