# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        dummy = head

        while dummy:
            nxt = dummy.next
            dummy.next = prev
            prev = dummy
            dummy = nxt

        return prev