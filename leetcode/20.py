# stack 활용하기
# valid parenthesis

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = ['(', '{', '[']
        pair = {'}': '{',
                ']': '[',
                ')': '('}
        
        for x in s:
            if x in open_brackets:
                stack.append(x)
                continue
            
            if len(stack) == 0:
                return False
            
            if stack.pop() != pair[x]:
                return False
            
        return len(stack) == 0