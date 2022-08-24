# binary search 응용문제
def isBadVersion(n):
  pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        def bsearch(start, end):
            if start == end:
                if isBadVersion(start):
                    return start
                else:
                    raise RuntimeError('wrong input')
            
            mid = start + (end-start)//2
            if isBadVersion(mid):
                return bsearch(start, mid)
            else:
                return bsearch(mid+1, end)
        
        return bsearch(0, n)