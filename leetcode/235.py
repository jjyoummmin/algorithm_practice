class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def find(node, small, big):
            if small <= node.val <= big:
                return node
            
            if node.val > big:
                return find(node.left, small, big)
            else:
                return find(node.right, small, big)
        
        s, b = min(p.val, q.val), max(p.val, q.val)
        
        return find(root, s, b)