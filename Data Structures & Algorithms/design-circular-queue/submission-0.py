class Node:
    def __init__(self, val, nxt=None, prv=None):
        self.val = val
        self.next = nxt
        self.prev = prv

class MyCircularQueue:

    def __init__(self, k: int):
        # [left]<->   [0] <-> [1] <-> [right]
        self.capacity = k 
        self.size = 0  # current size rn!
        self.left = Node(0)
        self.right = Node(0)

        self.left.next = self.right
        self.right.prev = self.left

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        # if full, return False

        # else
        # it would go in between right.prev and right
        # make a node = Node(val)
        # self.right.prev.next = node
        # node.prev = self.right.prev
        
        # node.next = self.right
        # self.right.prev = node
        # self.size += 1
        node = Node(value)
        tail = self.right.prev
        tail.next = node
        node.prev = tail

        self.right.prev = node
        node.next = self.right
        self.size += 1
        return True

    def deQueue(self) -> bool:
        # if empty, nothing to dequeue, return False
        if self.isEmpty(): return False
        
        # else
        # node = self.left.next
        # replacement = node.next
        # so self.left.next = replacement
        # replacement.prev = self.left
        # self.size -= 1

        to_remove = self.left.next
        new_head = to_remove.next
        self.left.next = new_head
        new_head.prev = self.left

        self.size -= 1 
        return True

    def Front(self) -> int:
        # if empty, return -1
        # return self.left.next.val
        if self.isEmpty(): return -1
        
        return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty(): return -1

        return self.right.prev.val
        # if empty, return -1
        # return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.size == 0
        # check if size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
        # check if size == cpacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()