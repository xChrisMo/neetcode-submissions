class Node:
    def __init__(self, val, key, prev=None, next=None):
      self.val=val
      self.key=key
      self.prev=prev
      self.next=next

class LRUCache:
    def __init__(self, capacity: int):
        # u want to use a doubly linked list to eep track of the LRU and MRU
        self.cap=capacity
        self.cache={}
        self.left=Node(0,0)
        self.right=Node(0,0)
        #connect them
        self.left.next=self.right
        self.right.prev=self.left
        
   
   #insert to the right
    def insert(self, node):
        prev=self.right.prev
        nxt=self.right
        prev.next=node
        node.next=nxt
        nxt.prev=node
        node.prev=prev
        
       
    def remove(self, node):
        prev=node.prev
        nxt=node.next
        prev.next=nxt
        nxt.prev=prev
        
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
       
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(value,key)
        self.insert(self.cache[key])
        if len(self.cache)>self.cap:
            lru=self.left.next
            del self.cache[lru.key]
            self.remove(lru)
        
        

        
    
        
        