# 연결리스트 palindrome
class Solution:
    def isPalindrome(self, head) -> bool:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        
        return l == l[::-1]