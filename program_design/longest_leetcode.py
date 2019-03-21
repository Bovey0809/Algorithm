def longestPalindrome(s: str):
    def grow(s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1, l, r  # r - 1 - (l+1) + 1
    _, l, r = max([grow(s, l, r) for l in range(len(s))
                   for r in (l, l+1)])
    return s[l+1: r]


longestPalindrome('abcccccdJIJIcbasdfsdf')
