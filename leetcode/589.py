# 트리 순회
# sol 1
class Solution:
    def preorder(self, root):
        result = []
        if root is None:
            return result
        
        result.append(root.val)
        for child in root.children:
            result += self.preorder(child)
        
        return result

# sol 2
class Solution:
    def preorder(self, root):
        def _pre(acc, node):
            if not node:
                return
            
            acc.append(node.val)
            for child in node.children:
                _pre(acc, child)
            return acc
        
    
        return _pre([], root)