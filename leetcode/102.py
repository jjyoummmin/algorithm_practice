# level order 트리 순회
from collections import deque

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        
        result = []
        queue = [root]
        
        while queue:
            current_level = []
            next_queue = []
            for node in queue:
                current_level.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            result.append(current_level)
            queue = next_queue
        return result