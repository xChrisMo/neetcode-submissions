"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        a hashmap that u map the ol one to the new one
        u wikl now use that hashmap to connect the next and random pointer
        '''

        oldToMap={None:None}
        cur=head
        while cur:
            new_node= Node(cur.val)
            oldToMap[cur]=new_node
            cur=cur.next
        cur=head
        while cur:
            copy=oldToMap[cur]
            copy.next=oldToMap[cur.next]
            copy.random=oldToMap[cur.random]
            cur=cur.next
        return oldToMap[head]
    