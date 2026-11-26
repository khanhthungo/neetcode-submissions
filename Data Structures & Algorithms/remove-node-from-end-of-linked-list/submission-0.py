# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head 
        s = dummy 
        f = head 
        moved = 0  
        while f and moved < n: 
            f = f.next 
            moved +=1 
        
        while f: 
            f = f.next 
            s = s.next 
        if s and s.next: 
            s.next = s.next.next 
        return dummy.next