import collections
class Solution:
    def findPairs(self, nums, k):
        c = collections.Counter(nums)

        return sum(k > 0 and i + k in c or k == 0 and c[i] > 1 for i in c)
        
my = Solution()
print(my.findPairs([1, -2, -3, 3, 4, 5, 8], 2))
