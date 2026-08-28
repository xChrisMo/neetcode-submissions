class Node:
    def __init__(self, val, key, prev=None, next=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={}
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left
   
    
    def insert(self, node):
        prev=self.right.prev
        next=self.right
        prev.next=node
        node.next=next
        next.prev=node
        node.prev=prev
       
    def remove(self, node):
        prev=node.prev
        nxt=node.next
        prev.next=nxt
        nxt.prev=prev
        

    def get(self, key: int) -> int:
        if key in self.cache:
            #remove then add to make it the most frequeunt
            nodeRem= self.cache[key]
            self.remove(nodeRem)
            self.insert(nodeRem)
            return self.cache[key].val
        return -1
      

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        new_node=Node(value,key)
        
        self.cache[key]= new_node
        self.insert(self.cache[key])
        if len(self.cache)>self.cap:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        
    
        
        