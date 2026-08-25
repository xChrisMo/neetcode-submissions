# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        cur=dummy
        right=head
        while right and n>0:
            right=right.next
            n-=1
        while right:
            cur=cur.next
            right=right.next
        cur.next=cur.next.next
        return dummy.next



        
       