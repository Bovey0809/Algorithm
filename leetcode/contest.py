from itertools import permutations
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        m = len(s1)
        if s1 >= s2:
            return all([s1[i] >= s2[i] for i in range(m)])
        return all(all([s1[i] <= s2[i] for i in range(m)]))

    
my = Solution()
print(my.checkIfCanBreak("yopumzgd","pamntyya"))