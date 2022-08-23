# 짝수 -> 그대로 더함 + 홀수 -> 짝수 개수만큼만 더함 + odd 1개까지 가능
from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        p_length = has_odd = 0
        for char in c:
            if c[char] % 2 == 0:
                p_length += c[char]
            else:
                p_length += c[char] - 1
                has_odd = 1
                
        
        return p_length + has_odd