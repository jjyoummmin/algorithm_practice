# sol 1) Counter 객체 이용하기
from collections import Counter

class Solution:
    def singleNumber(self, nums):
        c = Counter(nums)
        for key in c:
            if c[key] == 1:
                return key


# sol 2) Set 사용 (효율은 sol 1이 더 좋았음..)
class Solution:
    def singleNumber(self, nums):
        s = set()
        for n in nums:
            if n in s:
                s.remove(n)
            else:
                s.add(n)
        return s.pop()