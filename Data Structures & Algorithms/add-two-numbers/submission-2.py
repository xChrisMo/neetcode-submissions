# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        h1 = l1
        h2 = l2


        dummy = ListNode(0)
        curr = dummy

        while h1 or h2 or carry:
            h1_val = h1.val if h1 else 0
            h2_val = h2.val if h2 else 0
            
            val = carry + h1_val + h2_val
            carry = val // 10
            digit = val % 10

            node = ListNode(digit)
            h1 = h1.next if h1 else None
            h2 = h2.next if h2 else None

            curr.next = node
            curr = curr.next
        # how does the algorithm happen if l1 is done and l2 isnt ?
        # same but l2 is done, l1 isnt ?


        return dummy.next