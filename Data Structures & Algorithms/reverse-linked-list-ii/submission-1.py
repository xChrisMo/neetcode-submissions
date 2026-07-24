# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # create a dummy and make its next tge gead
        # set a 0 at dummy, 1 at head
        # move forward l - 1 times !

        # [X] [1] [2] [3] [4] [5]
        #          0   1 
        #         lp  curr  
        # [X] [1] [2]   [5] [4] [3]
        #          0   1

        # [X] [1] [2] [3] [4] [5]
        #  0   1

        # for i in range(l - 1)
        # so we now have our place to attach to the reverseal to, how then do we know where to stop ? or do we simply count?

        # for i in range(r - l + 1):
        # reverse

        dummy = ListNode(0, head)
        leftPrev = dummy
        curr = head

        # making left prev point to curr, then curr advancing...
        for i in range(left - 1):
            leftPrev = curr
            curr = curr.next

        prev = None
        for i in range(right - left + 1):
            nxt = curr.next # save
            curr.next = prev # flip pointer
            prev = curr # prev is now the curr 
            curr = nxt # curr is now the next

        leftPrev.next.next = curr # why ???
        leftPrev.next = prev

        return dummy.next
