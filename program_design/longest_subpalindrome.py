def longest_parlindrome(text):
    length = len(text)
    i = 1
    max_length = 0
    while i > 0 and i < 2*length-2:
        if i % 2 == 0:
            l = int(i/2-1)
            l, r = grow(text, l, l+2)
        else:
            l = int(i/2)
            l, r = grow(text, l, l+1)
        i += 1
        if (r-l) >= max_length:
            max_length = r-l
            start = l
            end = r+1
    return start, end


def grow(text, l, r):
    if text[l] != text[r]:
        return 0, 0
    while l >= 0 and r < len(text) and text[l].upper() == text[r].upper():
        l -= 1
        r += 1
    if r != len(text) and l != -1 and text[l] == text[r]:
        return l, r
    return l+1, r-1


def test():
    L = longest_parlindrome
    assert grow('ab', 0, 1) == (0, 0)
    assert grow('abccbd', 2, 3) == (1, 4)
    assert grow('abccba', 2, 3) == (0, 5)
    assert grow('kyabccba', 4, 5) == (2, 7)
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    print('Test Success!')


test()
