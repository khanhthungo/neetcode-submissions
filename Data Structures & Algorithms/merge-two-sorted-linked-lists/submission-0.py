# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy 
        l1 = list1 
        l2 = list2 
        while l1 and l2:
            newNode = ListNode()
            if l1.val <= l2.val: 
                newNode.val = l1.val 
                l1 = l1.next 
            else: 
                newNode.val = l2.val 
                l2 = l2.next 
            prev.next = newNode 
            prev = newNode
        
        if l1: 
            prev.next = l1 
        elif l2: 
            prev.next = l2 
        return dummy.next