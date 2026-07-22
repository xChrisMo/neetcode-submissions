# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # get to middle
        # # how do we handle even and odd ?
        # reverse from end to middle 

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next #, svae it!
        slow.next = None

        prev = None
        curr = second

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # so now we have the second half reversed, starting from prev!
        first = head # point to head, but we only add you up until second
        new = prev # pointing at the reversed head
        
        dummy = ListNode(0)
        tail = dummy
        

        while new:
            # tail.next = first
            # then second
            # then first... second, first, second

            nxtfirst = first.next
            nxtnew = new.next

            first.next = new
            new.next = nxtfirst

            first = nxtfirst
            new = nxtnew 