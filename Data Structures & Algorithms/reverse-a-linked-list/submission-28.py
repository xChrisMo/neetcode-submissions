# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # <-[1] [4]->[2]->[5]->[3]

        # [None]<-[1]<-[4]<-[2]<-[5]<-[3]
        #early exit
        if not head:
            return None

        prev = None
        curr = head

        while curr:
            temp = curr.next #store reference to next index
            curr.next = prev #flip the pointer to look at previons
            prev = curr
            curr = temp
            

        return prev



