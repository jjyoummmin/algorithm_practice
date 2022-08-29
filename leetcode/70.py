# fibonacci 응용
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        
        a, b = 1, 2
        for _ in range(n-1):
            a, b = b, a+b
        
        return a