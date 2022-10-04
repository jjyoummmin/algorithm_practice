from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        # 조건 
        # 앞에서 나열한 '(' 개수가 n보다 작으면 다음에 '('이 올 수 있다.
        # 앞에서 나열한 '(' 개수가 ')'보다 많으면 다음에 ')'가 올 수 있다.
        def helper(acc, n, open, close):
            if(open==close==n):
                result.append(acc)
                return
            if(open < n):
                helper(acc+'(', n, open+1, close)
            if(close < open):
                helper(acc+')', n, open, close+1) 
        
        helper('(', n, 1, 0)
        return result