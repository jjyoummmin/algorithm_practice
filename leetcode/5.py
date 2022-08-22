# 최대 길이인 팰린드롬 substring.
# 투 포인터 확장하기
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)

        def expand(left, right):
            if left < 0 or right >= length or s[left] != s[right]:
                return ''
            
            while left > 0 and right < length -1:
                if s[left -1] != s[right+1]:
                    break
                left -=1
                right += 1
            return s[left:right+1]
        
        max_p = ''
        for i, _ in enumerate(s):
            max_p = max(max_p, expand(i, i), expand(i, i+1), key=len)
        return max_p