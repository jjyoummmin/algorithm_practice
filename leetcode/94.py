class Solution:
    def inorderTraversal(self, root):
        if not root:
            return []
        
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        
        return left + [root.val] + right