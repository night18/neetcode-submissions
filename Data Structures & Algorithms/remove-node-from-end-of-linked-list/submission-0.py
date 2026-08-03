class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # MOVE THE RIGHT TO N
        while n > 0:
            right = right.next
            n -= 1
            
        # BOTH LEFT AND RIGHT ADD (LENGTH - N) STEP, AND RIGHT REACH THE END
        # THEN THE LEFT.NEXT IS THE INDEX WOULD LIKE TO DELETE
        while right:
            left = left.next
            right = right.next

        

        left.next = left.next.next
        return dummy.next