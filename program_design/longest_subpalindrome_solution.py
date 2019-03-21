def longest_subpalindrome_slice(text):
    "return (i, j) such the text[i:j] is the longest palindrome in text"
    if text == '':
        return (0, 0)

    candidates = [grow(text, start, end)
                  for start in range(len(text))
                  for end in (start, start+1)]
    return max(candidates, key=lambda a: a[1] - a[0])


def grow(text,  start, end):
    "start with a 0- or 1- length palindrome; try to grow a bigger one"
    while (start > 0 and end < len(text)
           and text[start - 1].upper() == text[end].upper()):
        start -= 1
        end += 1
    return (start, end)


def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == L('Racecar') == L('RacecarX') == (0, 7)
    print("Pass TEST")


test()
