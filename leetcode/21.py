# 두 정렬된 연결리스트 병합하기

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1 or not list2:
            return list1 or list2
        
        if list2.val < list1.val:
            list1, list2 = list2, list1
            
        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1