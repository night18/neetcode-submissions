# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        A = list1
        B = list2

        head = ListNode()
        curr = head

        while A is not None and B is not None:
            if A.val <= B.val:
                curr.next = A
                A = A.next
            else:
                curr.next = B
                B = B.next
            curr = curr.next

        curr.next = A if A is not None else B        
        # while A is not None:
        #     curr.next = A
        #     curr = curr.next
        #     A = A.next

        # while B is not None:
        #     curr.next = B
        #     curr = curr.next
        #     B = B.next

        return head.next