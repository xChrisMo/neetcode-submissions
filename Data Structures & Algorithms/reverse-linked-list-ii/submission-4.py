# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = head
        prevL = dummy

        for i in range(left-1):
            prevL = prevL.next
            curr = curr.next

        # gotten our reversal point
        prev = None
        for i in range(right - left + 1):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        prevL.next.next = curr
        prevL.next = prev

        return dummy.next