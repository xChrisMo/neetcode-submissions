# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dummy = head
        curr = dummy
        out = []
        length = 0

        while curr:
            out.append(curr.val)
            curr = curr.next
            length += 1

        max_sum = float('-inf')

        for i in range(length // 2):
            twin = length - 1 - i
            max_sum = max(max_sum, out[twin] + out[i])

        return max_sum

        #n = 20
        #l = 3
        #twin = 16