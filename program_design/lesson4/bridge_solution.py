# -----------------
# User Instructions
#
# Modify the bridge_problem(here) function so that it
# tests for goal later: after pulling a state off the
# frontier, not when we are about to put it on the
# frontier.


def bsuccessors(state):
    """Return a dict of {state:action} pairs.  A state is a (here, there, t) tuple,
    where here and there are frozensets of people (indicated by their times) and/or
    the light, and t is a number indicating the elapsed time."""
    here, there, t = state
    if 'light' in here:
        return dict(((here - frozenset([a, b, 'light']),
                      there | frozenset([a, b, 'light']),
                      t + max(a, b)),
                     (a, b, '->'))
                    for a in here if a != 'light'
                    for b in here if b != 'light')
    else:
        return dict(((here | frozenset([a, b, 'light']),
                      there - frozenset([a, b, 'light']),
                      t + max(a, b)),
                     (a, b, '<-'))
                    for a in there if a != 'light'
                    for b in there if b != 'light')


def elapsed_time(path):
    return path[-1][2]


def bridge_problem(here):
    """Modify this to test for goal later: after pulling a state off frontier,
    not when we are about to put it on the frontier."""
    # modify code below
    here = frozenset(here) | frozenset(['light'])
    explored = set()  # set of states we have visited
    # State will be a (people-here, people-there, time-elapsed)
    # ordered list of paths we have blazed
    frontier = [[(here, frozenset(), 0)]]
    if not here:
        return frontier[0]
    while frontier:
        path = frontier.pop(0)
        for (state, action) in bsuccessors(path[-1]).items():
            if state not in explored:
                here, there, t = state
                explored.add(state)
                path2 = path + [action, state]
                frontier.append(path2)

        frontier.sort(key=elapsed_time)
        if not frontier[0][0]:
            return frontier[-1]
    return []


def test():
    # the [-1][-1] grabs the total elapsed time
    assert bridge_problem(frozenset((1, 2),))[-1][-1] == 2
    assert bridge_problem(frozenset((1, 2, 5, 10),))[-1][-1] == 17
    return 'tests pass'


print(test())
