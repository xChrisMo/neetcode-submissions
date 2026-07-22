# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create a dummy node whose next is our head
        # start r from n,
        # start left from dummy

        # when r == None
        # left.next = left.next.next
        # return dummy.next

        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1


        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next