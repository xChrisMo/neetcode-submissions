class Node:
    def __init__(self, key, val, nxt=None, prv=None):
        self.key = key
        self.val = val
        self.next = nxt
        self.prev = prv

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

        self.map = {} # map, each key to its node 

        # [left] ->   <- [right]
        # add the mru behind between right.prev and right
        # get lru from left.next ?
    
    # UPDATE NODES WITH KEY !
    # this works because we know we would always have left and right as dummies....
    def remove(self, node):
        prv = node.prev
        nxt = node.next

        prv.next = nxt
        nxt.prev = prv

    def insert(self, node):
        # save the pointers irt self.right
        prv = self.right.prev
        nxt = self.right

        # link node's next and previous
        node.next = nxt
        node.prev = prv

        # reconnect disconnected pointers to include node!
        prv.next = node
        self.right.prev = node

    def get(self, key: int) -> int:
        # if not key[val], return -1
        # if key[val], return val
        if key not in self.map:
            return -1
    
        node = self.map[key]
        value = node.val
        
        self.remove(node) # removes it from whatever previous position
        self.insert(node) # adds it to mru ?

        return value

    def put(self, key: int, value: int) -> None:
        # if key, overwrite key with node of new value
        node = Node(key, value)

        if key in self.map:
            self.remove(self.map[key]) # removes former node and value
            self.map[key] = node # adds new node and value
            self.insert(node) # inserts new node and value
        
        else:
            self.map[key] = node
            self.insert(node)
            
        if len(self.map) > self.capacity:
            lru = self.left.next
            self.remove(lru)

            key = lru.key
            del self.map[key]
            


        # add key, Node(value)
        # if size > cpacity, remove lru
    # 
        
