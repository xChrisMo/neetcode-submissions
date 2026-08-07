# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        lp = dummy
        curr = head

        for i in range(left - 1):
            curr = curr.next
            lp = lp.next

        prev = None
        for _ in range(right - left + 1):
            tmp = curr.next
            curr.next = prev

            prev = curr
            curr = tmp

        lp.next.next = curr
        lp.next = prev
        return dummy.next