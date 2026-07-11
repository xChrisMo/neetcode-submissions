# <-       ->
# [] -> <- []
#   

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.cache = {} # key -> Node

        # creating our pointers
        self.right = Node(0, 0)
        self.left = Node(0, 0)
        
        # wiring up left and right
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        nxt = node.next
        prv = node.prev

        prv.next = nxt
        nxt.prev = prv

        # we have scrapped the node by moving the pointers aroubnd it 

    def insert(self, node):
        # insert RIGHT BEFORE right
        nxt = self.right
        previous = self.right.prev

        previous.next = node #this is very tricky, but it basically means the back pointer of RIGHT points towards the node ? feels wrong
        node.next = nxt

        node.prev = previous
        nxt.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        mru = self.cache[key]
        #so now we know it is infact inside the cache, it is the MRU
        # re remove its position inside the links
        self.remove(mru)

        # we insert it to be mru, right before right!
        self.insert(mru)
        # get the node, then the val
        return mru.val

    def put(self, key: int, value: int) -> None:
        # if in cache, we remove it from the list whereever it is
        if key in self.cache:
            self.remove(self.cache[key])
        
        # we make a new node, update the value in cache
        node = Node(key, value)
        # we addd it to our cache
        self.cache[key] = node

        # inserting to rightmost
        self.insert(node)

        # we check for overfill
        if len(self.cache) > self.cap:
            # meaning the node RIGHT AFTER left
            to_remove = self.left.next
            
            #i am picking this next var as where would skipp forward to from left,
            # marker = to_remove.next

            # self.left.next = marker
            # marker.prev = self.left
            
            # the above is TBD inside 'remove'! 
            self.remove(to_remove)
            del self.cache[to_remove.key]



        # to remove, we make self.left point to what is AFTER the node
        # 
