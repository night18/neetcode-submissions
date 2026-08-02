# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        slow = head.next
        fast = head.next.next
        
        while fast is not None and slow is not None:
            if fast == slow:
                return True
            
            if fast.next:
                fast = fast.next.next
                slow = slow.next
            else:
                return False


        return False