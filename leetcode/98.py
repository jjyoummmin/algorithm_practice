# 유효한 BST 인지 판별하기

import sys

class Solution:
    def isValidBST(self, root) -> bool:
        def dfs_in_range(node, start, end):
            if not node:
                return True
            if node.val <= start or node.val >= end:
                return False
            
            left_valid = dfs_in_range(node.left, start, node.val)
            right_valid = dfs_in_range(node.right, node.val, end)
            
            return left_valid and right_valid
        
        return dfs_in_range(root, -sys.maxsize, sys.maxsize)