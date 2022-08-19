# 연결리스트의 중간 노드 찾기 : fast, slow 투 포인터 사용하기
class Solution:
    def middleNode(self, head):
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow