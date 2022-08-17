from collections import defaultdict

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        length = len(s)      
        if length==0:
          return True
            
        index = 0
        for x in t:              
            if s[index] == x:
                index += 1
                if index == length:
                  return True
        return False