# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # so we set a previous
        # have a pointer to head (curr)
        # save the first next
        # point the curr = None
        # move prev to curr
        # curr = next
        # so we return prev
        # that is the new head

        curr = head
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev