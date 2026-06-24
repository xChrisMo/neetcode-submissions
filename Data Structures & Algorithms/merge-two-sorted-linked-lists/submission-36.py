# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # make a dummy to hang next values 
        # use a while condition to say, while both exist, take the miniumum, else add
        # move forwarda after picking from either lists
        # 
        curr_1 = list1
        curr_2 = list2

        if not curr_1 and not curr_2:
            return curr_1
            

        if not curr_1:
            return curr_2 
            
        if not curr_2:
            return curr_1

        dummy= ListNode()
        tail = dummy

        while curr_1 and curr_2:
            if curr_1.val < curr_2.val:
                tail.next = curr_1
                curr_1 = curr_1.next

            else:
                tail.next = curr_2
                curr_2 = curr_2.next
            
            tail = tail.next


        if curr_1:
            tail.next = curr_1

        if curr_2:
            tail.next = curr_2

        return dummy.next
        # referencing the start of 'tail'