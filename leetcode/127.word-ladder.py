#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
# https://leetcode.com/problems/word-ladder/description/
#
# algorithms
# Medium (25.88%)
# Likes:    2193
# Dislikes: 963
# Total Accepted:    340K
# Total Submissions: 1.3M
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# the length of shortest transformation sequence from beginWord to endWord,
# such that:
#
#
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
#
#
# Note:
#
#
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
#
#
# Example 1:
#
#
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output: 5
#
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" ->
# "dog" -> "cog",
# return its length 5.
#
#
# Example 2:
#
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: 0
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible
# transformation.
#
#
#
#
#
#

# @lc code=start

from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        def newWord(beginWord, endWord):
            for i in range(len(beginWord)):
                yield beginWord[:i]+endWord[i]+beginWord[i+1:]
        queue = deque([(beginWord, 1)])
        while queue:
            word, depth = queue.popleft()
            if word == endWord:
                return depth
            for new_word in newWord(word, endWord):
                if new_word in wordList:
                    queue.append((new_word, depth+1))
                    wordList.remove(new_word)
        return 0
# @lc code=end

me = Solution()
me.ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"])
