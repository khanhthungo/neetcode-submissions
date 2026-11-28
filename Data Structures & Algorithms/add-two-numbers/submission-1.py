# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        start = dummy 
        c = 0 
        while l1 and l2: 
            node = ListNode()
            val = c + l1.val + l2.val 
            node.val = val % 10 
            c = val // 10 
            start.next = node 
            start = node 
            l1 = l1.next 
            l2 = l2.next 
        
        while l1: 
            start.next = l1 
            start = l1 
            val = l1.val + c 
            l1.val = val %10 
            c = val //10 
            l1 = l1.next
        while l2: 
            start.next = l2 
            start = l2
            val = l2.val + c 
            l2.val = val %10 
            c = val //10 
            l2 = l2.next 

        while c != 0: 
            node = ListNode() 
            node.val = c % 10 
            c = c//10 
            start.next = node 
            start = node 
        return dummy.next


