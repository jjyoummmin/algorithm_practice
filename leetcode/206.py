# 연결리스트 역순으로 바꾸기
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        reversed = None
        while head:
            head.next, reversed, head = reversed, head, head.next
        return reversed