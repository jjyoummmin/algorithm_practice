# cycle이 시작되는 노드 찾기.
class Solution:
    def detectCycle(self, head):
        visited_node = set()
        
        while head:
            if head in visited_node:
                return head
            
            visited_node.add(head)
            head = head.next
        return None