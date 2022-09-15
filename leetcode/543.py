# 포인트는 None인 노드의 리턴값을 -1로 할 것!
# 그래야 leaf 에서 
# diameter = -1 + -1 + 2 = 0
# depth = max(-1, -1) + 1 = 0

class Solution:
    diameter = 0
    
    def diameterOfBinaryTree(self, root) -> int:
        def depth(node):
            if not node:
                return -1
            
            left = depth(node.left)
            right = depth(node.right)
            
            self.diameter = max(self.diameter, left+right+2)
            return max(left, right)+1
        
        depth(root)
        return self.diameter