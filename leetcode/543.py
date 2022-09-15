class Solution:
    diameter = 0
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            if not node:
                return -1
            
            left = depth(node.left)
            right = depth(node.right)
            
            self.diameter = max(self.diameter, left+right+2)
            return max(left, right)+1
        
        depth(root)
        return self.diameter