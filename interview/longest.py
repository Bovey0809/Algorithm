import sys


def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    # for i, v in enumerate(lines):
    print(longestPalindrome(str(lines[0])))


def longestPalindrome(s):

    length = len(s)

    def grow(st, e):
        while st >= 0 and e < length and s[st] == s[e]:
            st -= 1
            e += 1
        return s[st+1:e]
    output = max([grow(st, e) for st in range(length)
                  for e in (st, st+1)], key=len)
    return output if length > 1 else s


def longestPalindrome2(s):
    T = '#'.join('^{}$'.format(s))
    n = len(T)
    P = [0] * n
    C = R = 0
    for i in range(1, n-1):
        P[i] = (R > i) and min(R - i, P[2*C - i])  # equals to i' = C - (i-C)
        # Attempt to expand palindrome centered at i
        while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
            P[i] += 1

        # If palindrome centered at i expand past R,
        # adjust center based on expanded palindrome.
        if i + P[i] > R:
            C, R = i, i + P[i]

    # Find the maximum element in P.
    maxLen = max(P)
    for ind in P:
        if ind == maxLen:
            centerIndex = ind
            break
    return s[(centerIndex - maxLen)//2: (centerIndex + maxLen)//2]


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    print(lines)
    main(lines)
