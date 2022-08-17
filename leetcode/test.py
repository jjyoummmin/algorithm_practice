from collections import defaultdict

class Solution:       
    def isIsomorphic(self, s: str, t: str) -> bool:
      s1, s2, s3 = set(), set(), defaultdict(str)
      for x, y in zip(s,t):
        if x in s1 or y in s2:
          if s3[x] != y:
            return False
        else:
          s1.add(x)
          s2.add(y)
          s3[x] = y
      return True


result = Solution().isIsomorphic("badc", "baba")
print(result)