# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        split the array into half
        reverse the second half
        then do the connection
        '''
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        sec=slow.next
        slow.next=None
        cur=head

        prev=None
        while sec:
            tmp=sec.next
            sec.next=prev
            prev=sec
            sec=tmp

        while prev:
            tmp=cur.next
            tmp2=prev.next
            cur.next=prev
            prev.next=tmp
            cur=tmp
            prev=tmp2


